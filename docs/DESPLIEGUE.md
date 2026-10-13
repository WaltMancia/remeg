# Despliegue y dominio

> Esta guía se completa con los pasos reales a medida que se compra y conecta el dominio.

## Resumen de la arquitectura
- **Dominio:** `remeg.com.gt`, registrado en el registro oficial (www.gt, Universidad del Valle de Guatemala). Titular nacional: USD 20/año. Pago con tarjeta de crédito física o depósito en dólares. Los cambios de servidores DNS se solicitan por correo desde el contacto administrativo.
- **Alojamiento:** Netlify (plan gratuito), publicando la carpeta `site/`.
- **DNS:** proveedor gratuito a definir (Netlify DNS o Cloudflare).

## Pasos
1. Verificar disponibilidad de `remeg.com.gt` en www.gt.
2. Registrar el dominio a nombre de la empresa (razón social, NIT, contacto administrativo con correo propio de la empresa).
3. Crear la cuenta de Netlify a nombre de la empresa (2FA activado) y desplegar el repositorio.
4. Antes de cambiar servidores DNS, revisar los registros existentes para no afectar otros servicios (correo del dominio, etc.).
5. Solicitar al registro la delegación a los servidores de nombres elegidos; la propagación puede tardar de 24 a 48 horas.
6. Añadir `remeg.com.gt` y `www.remeg.com.gt` en Netlify; comprobar que ambos cargan y que HTTPS está activo.
7. Verificar formulario, enlaces y metadatos en producción.

## Datos que debe guardar la empresa
Cuenta del registro y recibo de caja, correo del contacto administrativo, cuenta de Netlify, cuenta de Umami y quién tiene acceso a cada una.

## Reversión
En Netlify: *Deploys* → elegir un despliegue anterior → *Publish deploy*.
