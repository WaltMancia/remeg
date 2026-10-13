# Resultados de pruebas — 12-oct-2026 (suite reproducible: `python3 tests/e2e.py`, 35/35) (Chromium headless/Playwright, servidor local sin compresión ni CDN)

## Aprobado
- Sin desbordamiento horizontal ni errores de consola/red a 360, 390, 768, 1280 y 1440 px (inicio y privacidad).
- Íconos: todos los `<use>` apuntan a un símbolo existente; 15 íconos en servicios/proceso/sectores.
- Enlaces tel, WhatsApp, mailto y mapa (coordenadas 14.6255, -90.4993) bien formados; anclas internas válidas.
- Menú móvil, galería (8 fotos con pies descriptivos y visor con teclado), botón flotante de WhatsApp (oculto arriba, aparece al desplazarse, solo en escritorio), detalle de pasos del proceso al pasar el cursor (0 → 171 px) y con foco de teclado.
- Formulario (servidor simulado): obligatorios, teléfono/correo, error 500 conserva datos, éxito limpia, 8 campos + `form-name`.
- Analítica con script simulado: se registran `click_llamar`, `click_whatsapp`, `click_correo`, `click_mapa` y `form_enviado`, sin datos personales; sin ID configurado no se carga ningún script externo.
- axe-core (WCAG 2.0/2.1/2.2 A y AA + buenas prácticas): 0 violaciones en 14 combinaciones (claro/oscuro × 360–1440 px, inicio y privacidad). Es una herramienta automática: no equivale a conformidad WCAG 2.2 AA.
- Lighthouse 13.5 (móvil simulado, local): Rendimiento 89, Accesibilidad 100, Buenas prácticas 100, SEO 100. FCP 0,9 s · LCP 2,7 s · CLS 0 · TBT 310 ms.

## No cumple / a vigilar
- LCP de laboratorio 2,7 s supera el objetivo de 2,5 s (medido en local, sin compresión ni CDN). Volver a medir en el sitio publicado; no son datos de usuarios reales.
- Una prueba automatizada del efecto hover falló una vez por el orden de la prueba; aislada, pasa.

## NO ejecutado / bloqueado
- Envío real y recepción en remeg2009@hotmail.com (requiere Netlify y notificación configurada).
- Registro de eventos en Umami real (requiere cuenta e ID).
- Firefox, Safari, teléfonos reales, lector de pantalla, Core Web Vitals de campo, dominio/HTTPS/indexación.
