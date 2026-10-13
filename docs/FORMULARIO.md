# Formulario de solicitud de servicio y cotización

## Cómo funciona
Formulario HTML con `data-netlify="true"` (nombre `cotizacion`). `site/assets/app.js` valida en el navegador y envía con `fetch` (POST a `/`). **Solo muestra la confirmación cuando Netlify responde con éxito**; si falla, conserva los datos y ofrece llamar o escribir por WhatsApp. Protección contra spam: campo trampa `bot-field` (los robots lo rellenan).

Campos: Nombre*, Empresa, Teléfono*, Correo, Servicio requerido*, Descripción del problema* (máx. 1000 caracteres), Potencia del motor, Voltaje. (* obligatorio)

## Configurar la recepción (una sola vez)
1. Desplegar el sitio en Netlify. En *Forms* debe aparecer `cotizacion`.
2. *Forms → Form notifications → Add notification → Email notification* → `remeg2009@hotmail.com`.
3. Enviar una solicitud real desde el sitio **publicado**.
4. Revisar la bandeja de entrada y la carpeta de correo no deseado de Hotmail/Outlook; si cae en spam, marcarla como "no es spam" y añadir el remitente de Netlify a contactos.

## Probar
- Local: no envía (muestra el aviso de error). Es el comportamiento esperado.
- Publicado: enviar una solicitud con datos de prueba y verificar que aparece en *Forms → Submissions* y llega al correo.

## Límites
En el plan gratuito de Netlify, el uso se mide en créditos (hay un tope mensual y el sitio se pausa si se agota). Las fuentes consultadas se contradicen sobre si los envíos de formulario consumen créditos: confirmarlo en la página de planes de Netlify antes de lanzar.
