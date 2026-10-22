# Sistema de diseño

Variables en `site/assets/styles.css` (`:root`, con redefinición para modo oscuro).

- **Colores:** ver tabla del README. Valores tomados del PDF de la empresa; son aproximaciones. Enlaces y botones usan `--lnk` y `--btnbg` para mantener el contraste AA en ambos temas.
- **Tipografía:** pila del sistema (sin fuentes externas); títulos en *Arial Narrow* con alternativa a Arial.
- **Íconos:** símbolos SVG en línea (sprite al inicio de `index.html`), trazo de 1,8 px, `currentColor`.
- **Componentes:** botones (`.btn .p/.s/.wa`), tarjetas de servicio (`.card`), franja de emergencias/horario (`.band`), galería (`.gal`), pasos del proceso (`.steps`), formulario, visor modal (`<dialog>`).
- **Movimiento:** transiciones breves; se desactivan con `prefers-reduced-motion`.
- **Imágenes:** fotografías propias de REMEG en WebP (hero 1000 px; resto máx. 900 px). Hero: `hero-motor-instalado`. Carrusel de rebobinado (`rebobinado-NN`) con desplazamiento por *scroll-snap* y botones; sin reproducción automática. La galería `taller-NN` muestra hasta 8 fotos y solo presenta *Ver todas* cuando hay más de 8, con el total renderizado. No hay imágenes de stock.
