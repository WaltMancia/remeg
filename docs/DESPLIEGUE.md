# Despliegue y dominio

Estado: dominio `remeg.com.gt` registrado (1 año). Sitio por publicar en Netlify.

## Arquitectura
- **Dominio:** `remeg.com.gt`, registro oficial .gt (Universidad del Valle de Guatemala, www.gt). Tarifa nacional: USD 20/año, igual en la renovación.
- **Alojamiento:** Netlify (plan gratuito), publicando la carpeta `site/` desde la rama `main` de este repositorio.
- **DNS:** Cloudflare (plan gratuito), solo como servidor de nombres. Motivo: el registro .gt solo delega servidores de nombres, y Cloudflare permite apuntar el dominio raíz (`remeg.com.gt`) a Netlify mediante *CNAME flattening*, opción que Netlify documenta. No se activa el proxy de Cloudflare (nube gris, "solo DNS").

## Fases
1. **Desplegar en Netlify** y probar en la dirección `*.netlify.app` (sitio, formulario real, notificación por correo).
2. **Consultar los datos del dominio** en www.gt (estado, contactos, servidores de nombres actuales).
3. **Crear la zona en Cloudflare** (plan Free) y copiar sus dos servidores de nombres.
4. **Solicitar al registro el cambio de servidores DNS**, por correo, desde el contacto administrativo o técnico registrado. El dominio debe estar en estado *Registrado*; la replicación tarda de 24 a 48 horas.
5. **Crear los registros** en Cloudflare (ver abajo) y **añadir el dominio en Netlify**.
6. **HTTPS y verificación** con y sin `www`.

## Registros DNS (valores a confirmar en el panel de Netlify antes de crearlos)
| Tipo | Nombre | Destino | Proxy |
|---|---|---|---|
| CNAME | `@` | `apex-loadbalancer.netlify.com` | Solo DNS (nube gris) |
| CNAME | `www` | `<nombre-del-sitio>.netlify.app` | Solo DNS (nube gris) |

Alternativa para el dominio raíz si no se usa *flattening*: registro **A** `@` → `75.2.60.5` (IP del balanceador de Netlify; confirmar el valor vigente en la documentación de Netlify).

En Netlify: *Domain management → Add a domain* con `remeg.com.gt`; dejarlo como dominio **principal** (coincide con la URL canónica del sitio) y `www.remeg.com.gt` como alias, que redirige al principal. Netlify emite el certificado HTTPS cuando el DNS ya apunta a su plataforma.

## Antes de modificar DNS
- Anotar los servidores de nombres y registros actuales del dominio (por si hubiera que volver atrás).
- Confirmar que no hay otro servicio que dependa del dominio (correo con el dominio, otro sitio). Hoy el correo de la empresa es `remeg2009@hotmail.com`, que no depende de este dominio.
- Al cambiar de servidores DNS, el registro pide que el proveedor anterior elimine la información del dominio y que en los nuevos servidores se creen las zonas necesarias.

## Datos que debe guardar la empresa
Recibo del registro, correo del contacto administrativo y técnico, fecha de vencimiento del dominio, cuenta de Netlify, cuenta de Cloudflare, cuenta de Umami y quién tiene acceso a cada una. Activar verificación en dos pasos en todas.

## Renovación (importante)
El dominio se registró por **un año**. Si no se renueva, se pierde el dominio y con él el sitio y su posicionamiento. Poner un recordatorio de calendario 45 y 15 días antes del vencimiento. La renovación se paga en el sitio del registro (USD 20 al año según su tabla de tarifas) y los datos de contacto deben estar al día.

## Consumo de Netlify (plan gratuito)
El plan gratuito usa un tope mensual de créditos y pausa el sitio si se agotan. Cada despliegue a producción consume créditos: agrupar los cambios antes de subirlos a `main` y desactivar las vistas previas innecesarias. Confirmar las cifras vigentes en la página de planes de Netlify.

## Reversión
En Netlify: *Deploys* → elegir un despliegue anterior → *Publish deploy*. Para volver a los servidores DNS anteriores, solicitar el cambio de nuevo al registro.
