# REMEG · Sitio web corporativo

Landing page profesional de **REMEG — Rebobinado de Motores Eléctricos de Guatemala**, orientada a generar llamadas, mensajes de WhatsApp y solicitudes de cotización de clientes industriales.

> **Soluciones confiables para mantener su industria en movimiento.**

| | |
|---|---|
| **Sitio** | https://remeg.com.gt *(pendiente de registrar y conectar; ver [estado](#estado-del-proyecto))* |
| **Tipo** | Sitio estático (HTML + CSS + JavaScript), sin dependencias ni paso de compilación |
| **Alojamiento previsto** | Netlify (plan gratuito) |
| **Idioma** | Español (Guatemala) |

## Contenido

- [Estado del proyecto](#estado-del-proyecto)
- [Características](#características)
- [Tecnología y decisiones](#tecnología-y-decisiones)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Inicio rápido](#inicio-rápido)
- [Pruebas](#pruebas)
- [Configuración](#configuración)
- [Despliegue](#despliegue)
- [Diseño](#diseño)
- [Accesibilidad, SEO y rendimiento](#accesibilidad-seo-y-rendimiento)
- [Seguridad y privacidad](#seguridad-y-privacidad)
- [Mantenimiento: cómo editar el sitio](#mantenimiento-cómo-editar-el-sitio)
- [Hoja de ruta](#hoja-de-ruta)
- [Licencia](#licencia)

## Estado del proyecto

| Área | Estado |
|---|---|
| Landing page (todas las secciones), diseño responsive, íconos, galería | ✅ Implementado y probado en local |
| Política de privacidad | ⚠️ Borrador; **requiere revisión de REMEG y asesoría legal** antes de publicar |
| Formulario → `remeg2009@hotmail.com` | ⏳ Implementado; **falta desplegar en Netlify, configurar la notificación y hacer una prueba real de recepción** |
| Analítica (Umami Cloud) | ⏳ Implementada; **falta crear la cuenta y pegar el ID** |
| Dominio `remeg.com.gt` | ⏳ No registrado todavía |
| Publicación, HTTPS, indexación | ⏳ Pendiente (dependen del dominio y del despliegue) |

Lista completa de tareas abiertas: [`docs/PENDIENTES.md`](docs/PENDIENTES.md).

## Características

- **Conversión:** botones de *Solicitar cotización*, *Llamar* y *WhatsApp* (con mensaje inicial), barra de contacto fija en móvil y botón flotante de WhatsApp discreto en escritorio.
- **Emergencias y horario diferenciados:** emergencias 24 h / 365 días, y taller todos los días de 7:00 a. m. a 5:00 p. m.
- **Servicios:** rebobinado, mantenimiento preventivo y correctivo, medición de aislamiento con Megger, reparaciones mecánicas, recolección y entrega (como parte de la cotización).
- **Galería "Nuestro taller":** fotografías propias optimizadas (WebP), con pies descriptivos y visor accesible por teclado.
- **Proceso de trabajo** en 6 pasos con detalle al pasar el cursor o enfocar con teclado (siempre visible en pantallas táctiles).
- **Formulario** con 8 campos (4 obligatorios: nombre, teléfono, servicio y descripción), validación en el cliente, estados de carga y error sin perder datos, y protección contra spam por campo trampa.
- **SEO local:** metadatos, Open Graph, datos estructurados `LocalBusiness` con dirección, teléfonos, horario del taller y coordenadas confirmadas, `sitemap.xml` y `robots.txt`.
- **Analítica respetuosa con la privacidad:** Umami Cloud, sin cookies, sin datos personales en los eventos.
- **Modo claro y oscuro** automático según el sistema.

## Tecnología y decisiones

| Decisión | Motivo |
|---|---|
| HTML/CSS/JS sin framework | Una landing de una página no necesita React ni compilación: carga más rápido, es fácil de mantener por cualquier persona y no tiene dependencias que actualizar. |
| Netlify + Netlify Forms | Recibe el formulario sin servidor propio ni claves secretas; despliegue arrastrando la carpeta o desde GitHub. |
| Umami Cloud | Plan gratuito, sin cookies, con eventos personalizados (llamada, WhatsApp, formulario). |
| Íconos SVG propios en línea | Sin solicitudes externas ni librerías; heredan el color del texto. |
| CSS con variables (*tokens*) | Cambiar la paleta o el espaciado desde un solo lugar. |
| Política de seguridad de contenido (CSP) estricta | Solo se permiten recursos propios y el dominio de analítica. Por eso no hay estilos ni scripts en línea. |

## Estructura del repositorio

```
.
├── site/                      # Lo único que se publica
│   ├── index.html             # Landing: contenido, SEO y datos estructurados
│   ├── privacidad.html        # Política de privacidad (borrador)
│   ├── 404.html
│   ├── robots.txt
│   ├── sitemap.xml
│   └── assets/
│       ├── styles.css         # Diseño y variables (tokens)
│       ├── app.js             # Menú, galería, formulario, analítica
│       ├── logo.png           # Logotipo original de REMEG
│       ├── favicon.png
│       └── foto*.webp         # Fotografías optimizadas
├── docs/                      # Guías y pendientes
├── tests/                     # Pruebas automatizadas (Playwright + axe)
├── tools/optimize_images.py   # Convierte fotos a WebP para la web
├── netlify.toml               # Carpeta publicada, cabeceras de seguridad y caché
├── LICENSE
└── README.md
```

## Inicio rápido

No requiere instalar nada para ver el sitio:

```bash
git clone <URL-DEL-REPOSITORIO>
cd <carpeta>
python3 -m http.server 8000 -d site
# abrir http://localhost:8000
```

> En local el formulario **no envía** solicitudes (solo funciona en Netlify) y mostrará un aviso de error; no simula envíos exitosos.

## Pruebas

```bash
pip install -r tests/requirements.txt
playwright install chromium
python3 tests/e2e.py
```

La suite levanta un servidor local y comprueba: ausencia de desbordamiento y errores de consola en 5 anchos de pantalla, enlaces de llamada, WhatsApp y mapa, menú móvil, validaciones del formulario (con servidor simulado), galería, proceso, botón flotante, eventos de analítica (simulados) y accesibilidad automática con axe-core (claro y oscuro).

**Qué no cubre:** el envío real del formulario, la analítica real, Firefox/Safari, lectores de pantalla ni dispositivos físicos. Resultados detallados y límites: [`docs/PRUEBAS.md`](docs/PRUEBAS.md).

Lighthouse (opcional):

```bash
npx lighthouse http://localhost:8000 --only-categories=performance,accessibility,best-practices,seo --view
```

## Configuración

| Qué | Dónde | Guía |
|---|---|---|
| Recepción de solicitudes del formulario | Panel de Netlify → *Forms* → notificación por correo | [`docs/FORMULARIO.md`](docs/FORMULARIO.md) |
| Analítica | `site/index.html`: `<meta name="umami-website-id" content="">` | [`docs/ANALITICA.md`](docs/ANALITICA.md) |
| Dominio y DNS | Registro .gt + proveedor de DNS | [`docs/DESPLIEGUE.md`](docs/DESPLIEGUE.md) |

Este proyecto **no usa secretos ni variables de entorno**: no hay claves en el código.

## Despliegue

Resumen (detalle en [`docs/DESPLIEGUE.md`](docs/DESPLIEGUE.md)):

1. Crear una cuenta de Netlify a nombre de la empresa y activar la verificación en dos pasos.
2. *Add new site → Import from Git* (o arrastrar la carpeta `site/`). `netlify.toml` ya indica `publish = "site"`.
3. Configurar la notificación de correo del formulario `cotizacion` y **enviar una solicitud real de prueba**.
4. Conectar `remeg.com.gt` y activar HTTPS.
5. Verificar el sitio publicado (enlaces, formulario, metadatos) y enviar el sitemap a Google Search Console.

Reversión: en Netlify, *Deploys → Publish deploy* sobre un despliegue anterior.

## Diseño

Identidad derivada del material de marca de REMEG (azules corporativos). Los valores son aproximaciones tomadas del PDF de la empresa.

| Token | Valor | Uso |
|---|---|---|
| `--navy` | `#0F3D89` | Encabezado, fondos de contraste |
| `--ink` | `#0B2559` | Hero, pie de página |
| `--blue` | `#1650B8` | Botones y enlaces (modo claro) |
| `--sky` | `#85A8D7` | Detalles, bordes, énfasis |
| `--mist` | `#EAF1FB` | Fondos secundarios |
| WhatsApp | `#0A7D3C` | Botones de WhatsApp (contraste AA con texto blanco) |
| Alerta | `#F2B705` | Indicador de emergencias y foco de teclado |

Más detalles en [`docs/DISENO.md`](docs/DISENO.md).

## Accesibilidad, SEO y rendimiento

Resultados **medidos** en laboratorio (Chromium local, móvil simulado, sin compresión ni CDN):

| Medición | Resultado |
|---|---|
| axe-core (WCAG 2.0/2.1/2.2 A y AA + buenas prácticas) | 0 violaciones en 14 combinaciones de pantalla y tema |
| Lighthouse 13.5 | Rendimiento 89 · Accesibilidad 100 · Buenas prácticas 100 · SEO 100 |
| FCP / LCP / CLS / TBT | 0,9 s / **2,7 s** / 0 / 310 ms |

- El **LCP de laboratorio (2,7 s) supera el objetivo de 2,5 s**; hay que volver a medirlo en el sitio publicado. No son datos de usuarios reales.
- Las herramientas automáticas **no demuestran** conformidad con WCAG 2.2 AA: falta revisión manual y con lector de pantalla.

## Seguridad y privacidad

- Cabeceras de seguridad y CSP en `netlify.toml`; HTTPS gestionado por Netlify.
- Sin cookies publicitarias ni píxeles de seguimiento. Los eventos de analítica no incluyen nombre, teléfono, correo ni descripciones.
- El formulario recoge solo lo necesario; correo, empresa, potencia y voltaje son opcionales.
- `site/privacidad.html` es un **borrador sin revisión legal**; los puntos a confirmar están al inicio del archivo.

## Mantenimiento: cómo editar el sitio

| Quiero cambiar… | Edite… |
|---|---|
| Textos, teléfonos, horarios, preguntas frecuentes | `site/index.html` |
| Colores, tipografía, espaciado | Variables en `site/assets/styles.css` (`:root`) |
| Fotografías | Optimizar con `python3 tools/optimize_images.py foto.jpg`, copiar a `site/assets/` y actualizar `src`, `width`, `height`, `alt` y pie de foto |
| Número o mensaje de WhatsApp | Buscar `wa.me/` en `site/index.html` |
| Coordenadas del taller | Datos estructurados (JSON-LD) y enlaces de mapa en `site/index.html` |
| Cuando se cambie el dominio | `canonical`, Open Graph, JSON-LD, `robots.txt` y `sitemap.xml` |

Después de cualquier cambio: ejecutar `python3 tests/e2e.py` y volver a desplegar (con Git conectado, cada *push* a `main` publica automáticamente).

## Hoja de ruta

1. Registrar el dominio, conectar el sitio y comprobar el formulario real.
2. Revisión legal de la política de privacidad.
3. Medir Core Web Vitals en el sitio publicado y optimizar el LCP si hace falta.
4. Revisión manual de accesibilidad (teclado, lector de pantalla, zoom 200 %).
5. Alta del perfil de Google Business (requiere acceso de la empresa).
6. Pruebas A/B o de usabilidad cuando haya tráfico suficiente.

## Licencia

Código, logotipo, fotografías y textos: © 2026 REMEG. Todos los derechos reservados. Licencia provisional; ver [`LICENSE`](LICENSE).
