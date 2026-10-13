# Analítica (Umami Cloud)

Sin cookies ni datos personales. Respeta la señal "No rastrear". El script solo se carga si `site/index.html` contiene un ID:

```html
<meta name="umami-website-id" content="PEGUE-AQUI-EL-ID">
```

## Configurar
1. Crear cuenta en https://umami.is y añadir el sitio `remeg.com.gt`.
2. Copiar el *Website ID* y pegarlo en la etiqueta anterior; redesplegar.
3. Verificar en *Realtime* y *Events*.

## Eventos
| Evento | Cuándo |
|---|---|
| (vista de página) | Cada visita |
| `click_llamar` | Clic en un enlace `tel:` |
| `click_whatsapp` | Clic en un enlace de WhatsApp |
| `click_correo` | Clic en un enlace `mailto:` |
| `click_mapa` | Clic en ubicación o "Cómo llegar" |
| `form_enviado` | Solo cuando el envío del formulario fue aceptado |

Ningún evento incluye nombre, teléfono, correo ni descripción.

## Notas
- La política de seguridad (`netlify.toml`) permite `cloud.umami.is` y `api-gateway.umami.dev`. Si Umami cambia sus dominios, actualizar `script-src` y `connect-src`.
- El plan gratuito tiene límite de eventos mensuales (alrededor de 100 mil según las fuentes consultadas) y 6 meses de historial: confirmar en la página de precios de Umami.
- Los eventos se probaron solo con un script simulado, no contra Umami real.
