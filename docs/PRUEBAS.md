# Resultados de pruebas — 14-oct-2026

Suite reproducible: `python3 tests/e2e.py` (Chromium/Playwright + axe-core, servidor local). **45 / 45 aprobadas.**

## Aprobado
- Sin desbordamiento horizontal ni errores de consola/red a 360, 390, 768, 1280 y 1440 px (inicio y privacidad).
- Íconos válidos; enlaces de llamada, WhatsApp, correo y mapa (coordenadas 14.6255, -90.4993); anclas internas; menú móvil.
- Formulario con servidor simulado: obligatorios, formatos, error 500 conserva datos, éxito limpia, 8 campos + `form-name`.
- Galería «Nuestro taller»: 11 fotos, 8 visibles, las nuevas primero, *Ver todas* / *Ver menos* con `aria-expanded`, visor con pie descriptivo y contador.
- Carrusel de rebobinado: 7 fotos, región accesible, botón anterior desactivado al inicio, «siguiente» desplaza, visor (1 de 7).
- Paso 5 con el texto de pruebas en vacío; hero con la foto nueva; botón flotante de WhatsApp; detalle del proceso con hover y teclado.
- Analítica con script simulado (5 eventos, sin datos personales); sin ID no carga scripts externos.
- axe-core (WCAG 2.0/2.1/2.2 A y AA + buenas prácticas): 0 violaciones en 14 combinaciones (claro/oscuro × pantallas). Herramienta automática: no equivale a conformidad WCAG 2.2 AA.
- Lighthouse 13.5 (móvil simulado, local): Rendimiento 91 · Accesibilidad 100 · Buenas prácticas 100 · SEO 100. FCP 1,8 s · LCP 2,7 s · CLS 0 · TBT 170 ms.

## No cumple / a vigilar
- LCP de laboratorio 2,7 s supera el objetivo de 2,5 s (medido en local, sin compresión ni CDN). Volver a medir en el sitio publicado; no son datos de usuarios reales.

## No ejecutado / bloqueado
- Envío real y recepción en remeg2009@hotmail.com (requiere Netlify y notificación configurada).
- Registro de eventos en Umami real (requiere cuenta e ID).
- Firefox, Safari, teléfonos reales, lector de pantalla, Core Web Vitals de campo, dominio/HTTPS/indexación.
