#!/usr/bin/env python3
"""Pruebas de humo automatizadas del sitio (Playwright + axe-core).

Uso:
    pip install -r tests/requirements.txt && playwright install chromium
    python3 tests/e2e.py

Levanta un servidor local sobre site/, ejecuta las comprobaciones y termina con código 1 si alguna falla.
NO prueba el envío real del formulario ni la analítica real: ambos se simulan.
"""
import subprocess, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright
from axe_playwright_python.sync_playwright import Axe

SITE = Path(__file__).resolve().parent.parent / "site"
PORT = 8765
U = f"http://localhost:{PORT}/"
res = []

def ok(name, cond, extra=""):
    res.append(bool(cond))
    print(("PASS" if cond else "FAIL"), name, extra)

def main():
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "-d", str(SITE)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for w, h in [(360, 740), (390, 844), (768, 1024), (1280, 800), (1440, 900)]:
                pg = b.new_page(viewport={"width": w, "height": h})
                errs, bad = [], []
                pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
                pg.on("pageerror", lambda e: errs.append(str(e)))
                pg.on("response", lambda r: bad.append(r.url) if r.status >= 400 else None)
                for path in ("", "privacidad.html"):
                    pg.goto(U + path); pg.wait_for_load_state("networkidle")
                    ok(f"{w}px /{path} sin desbordamiento horizontal", pg.evaluate("document.documentElement.scrollWidth<=innerWidth"))
                ok(f"{w}px sin errores de consola/red", not errs and not bad, str(errs + bad))
                pg.close()

            pg = b.new_page(viewport={"width": 390, "height": 844}); pg.goto(U)
            ok("íconos: cada <use> apunta a un símbolo", pg.evaluate("[...document.querySelectorAll('use')].every(u=>document.querySelector(u.getAttribute('href')))"))
            ids = pg.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].map(a=>a.getAttribute('href').slice(1)).filter(i=>i&&!document.getElementById(i))")
            ok("anclas internas válidas", not ids, str(ids))
            ok("enlaces de mapa con las coordenadas confirmadas", pg.evaluate("[...document.querySelectorAll('a[href*=\"google.com/maps\"]')].every(a=>a.href.includes('14.6255,-90.4993'))"))
            ok("enlaces tel/WhatsApp correctos", pg.evaluate("[...document.querySelectorAll('a[href^=tel],a[href*=\"wa.me\"]')].every(a=>/tel:\\+502472648|tel:\\+502471546|wa\\.me\\/50247264881\\?text=/.test(a.href))"))
            pg.click("#mb"); ok("menú móvil abre", pg.get_attribute("#mb", "aria-expanded") == "true")
            pg.keyboard.press("Escape"); ok("Escape cierra el menú", pg.get_attribute("#mb", "aria-expanded") == "false")

            # Formulario (servidor simulado)
            pg.click("#sb"); ok("campos obligatorios vacíos bloquean el envío", pg.evaluate("document.querySelectorAll('[aria-invalid=true]').length") == 4)
            ok("correo es opcional", pg.get_attribute("#e", "aria-invalid") == "false")
            pg.fill("#n", "Prueba"); pg.fill("#t", "123"); pg.select_option("#sv", index=1); pg.fill("#d", "Motor con ruido"); pg.fill("#e", "mal")
            pg.click("#sb"); ok("teléfono corto y correo inválido rechazados", pg.get_attribute("#t", "aria-invalid") == "true" and pg.get_attribute("#e", "aria-invalid") == "true")
            pg.fill("#t", "4726 4881"); pg.fill("#e", "")
            pg.route("**/", lambda r: r.fulfill(status=500) if r.request.method == "POST" else r.continue_())
            pg.click("#sb"); pg.wait_for_function("document.querySelector('#st').className=='bad'")
            ok("fallo del servicio: error visible y datos conservados", pg.input_value("#n") == "Prueba" and "No pudimos" in pg.inner_text("#st"))
            pg.unroute("**/"); sent = []
            pg.route("**/", lambda r: (sent.append(r.request.post_data), r.fulfill(status=200, body="ok")) if r.request.method == "POST" else r.continue_())
            pg.click("#sb"); pg.wait_for_function("document.querySelector('#st').className=='ok'")
            ok("éxito simulado: confirmación y formulario limpio", pg.input_value("#n") == "" and "REMEG se pondrá" in pg.inner_text("#st"))
            ok("el envío incluye los 8 campos y form-name", sent and all(k in sent[0] for k in ["form-name=cotizacion", "nombre=", "telefono=", "correo=", "servicio=", "descripcion=", "potencia=", "voltaje=", "empresa="]))

            # Galería, proceso, botón flotante
            # Galería "Nuestro taller": 11 fotos, 8 visibles, el resto con "Ver todas"
            ok("galería: 11 fotos y solo 8 visibles al inicio", pg.evaluate("document.querySelectorAll('#gal figure').length")==11 and pg.evaluate("document.querySelectorAll('#gal figure:not([hidden])').length")==8)
            ok("galería: las fotos nuevas van primero", pg.evaluate("document.querySelector('#gal img').getAttribute('src')")=="assets/taller-01.webp")
            pg.click("#gal figure >> nth=0 >> button"); ok("visor de galería con pie descriptivo", "Motor en maniobra con cadena" in pg.inner_text("#lc") and "1 de 11" in pg.inner_text("#lc"), pg.inner_text("#lc")); pg.keyboard.press("Escape")
            pg.click("#gm"); ok("«Ver todas»: muestra las 11 y marca aria-expanded", pg.evaluate("document.querySelectorAll('#gal figure:not([hidden])').length")==11 and pg.get_attribute("#gm","aria-expanded")=="true")
            pg.click("#gm"); ok("«Ver menos»: vuelve a 8", pg.evaluate("document.querySelectorAll('#gal figure:not([hidden])').length")==8)
            # Carrusel de rebobinado
            ok("carrusel: 7 fotos de rebobinado con región accesible", pg.evaluate("document.querySelectorAll('.car .track figure').length")==7 and pg.get_attribute(".car","role")=="region")
            ok("carrusel: botón anterior desactivado al inicio", pg.get_attribute(".cp","aria-disabled")=="true")
            pg.locator(".car").scroll_into_view_if_needed(); pg.click(".cn"); pg.wait_for_timeout(900)
            ok("carrusel: «siguiente» desplaza las fotos", pg.evaluate("document.querySelector('.track').scrollLeft")>50 and pg.get_attribute(".cp","aria-disabled")=="false")
            pg.click(".car .track figure >> nth=0 >> button"); ok("visor del carrusel (1 de 7)", "1 de 7" in pg.inner_text("#lc"), pg.inner_text("#lc")); pg.keyboard.press("Escape")
            # Contenido solicitado por el cliente
            ok("paso 5: pruebas en vacío con el motor energizado", "Se energiza el motor para realizar pruebas en vacío antes de su entrega." in pg.inner_text("#steps"))
            ok("hero con la foto nueva", pg.evaluate("document.querySelector('.hero img').getAttribute('src')")=="assets/hero-motor-instalado.webp")
            d = b.new_page(viewport={"width": 1280, "height": 800}); d.goto(U)
            ok("botón flotante de WhatsApp oculto arriba", not d.is_visible("#waf"))
            d.mouse.wheel(0, 1500); d.wait_for_timeout(600); ok("botón flotante aparece al desplazarse", d.is_visible("#waf"))
            d.goto(U); li = d.locator("#steps li").first; li.scroll_into_view_if_needed()
            h0 = li.locator(".dt").evaluate("e=>e.getBoundingClientRect().height"); li.hover(); d.wait_for_timeout(600)
            ok("proceso: el detalle se revela con hover", li.locator(".dt").evaluate("e=>e.getBoundingClientRect().height") > h0 + 10)
            li2 = d.locator("#steps li").nth(1); d.mouse.move(0, 0); li2.focus(); d.wait_for_timeout(500)
            ok("proceso: el detalle se revela con foco de teclado", li2.locator(".dt").evaluate("e=>e.getBoundingClientRect().height") > 10)

            # Analítica simulada
            html = (SITE / "index.html").read_text().replace('name="umami-website-id" content=""', 'name="umami-website-id" content="TEST-ID"')
            a = b.new_page(viewport={"width": 390, "height": 844})
            a.route(U, lambda r: r.fulfill(status=200, content_type="text/html", body=html) if r.request.method == "GET" else r.fulfill(status=200, body="ok"))
            a.route("https://cloud.umami.is/script.js", lambda r: r.fulfill(status=200, content_type="text/javascript", body="window.__ev=[];window.umami={track:n=>window.__ev.push(n)}"))
            a.goto(U); a.wait_for_timeout(400)
            a.evaluate("document.querySelectorAll('a').forEach(x=>x.addEventListener('click',e=>e.preventDefault()))")
            for sel in [".hero a[href^=tel]", ".hero a[href*='wa.me']", "#contacto a[href^=mailto]", "#contacto a[href*='google.com/maps'] >> nth=0"]: a.click(sel)
            a.fill("#n", "Prueba"); a.fill("#t", "47264881"); a.select_option("#sv", index=1); a.fill("#d", "texto privado"); a.click("#sb")
            a.wait_for_function("document.querySelector('#st').className=='ok'")
            ev = a.evaluate("window.__ev")
            ok("eventos de analítica registrados (script simulado)", ev == ["click_llamar", "click_whatsapp", "click_correo", "click_mapa", "form_enviado"], str(ev))
            pg2 = b.new_page(); pg2.goto(U)
            ok("sin ID configurado no carga scripts externos", not pg2.evaluate("[...document.scripts].some(s=>s.src.includes('umami'))"))

            # Accesibilidad automática (axe)
            axe, total = Axe(), 0
            for scheme in ("light", "dark"):
                for w, path in [(360, ""), (390, ""), (768, ""), (1280, ""), (1440, ""), (390, "privacidad.html"), (1280, "privacidad.html")]:
                    x = b.new_page(viewport={"width": w, "height": 900}, color_scheme=scheme); x.goto(U + path); x.wait_for_timeout(250)
                    v = axe.run(x, options={"runOnly": {"type": "tag", "values": ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa", "best-practice"]}}).response["violations"]
                    total += len(v)
                    if v: print("   axe", scheme, w, path, [(i["id"], len(i["nodes"])) for i in v])
                    x.close()
            ok("axe-core: 0 violaciones (claro/oscuro × 7 combinaciones)", total == 0, f"({total})")
            b.close()
    finally:
        srv.terminate()
    print(f"\n{sum(res)} / {len(res)} comprobaciones aprobadas")
    sys.exit(0 if all(res) else 1)

if __name__ == "__main__":
    main()
