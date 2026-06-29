# Última Sesión - Bar Luna Llena

## Qué se ha hecho hoy
- Se corrigió el desbordamiento del logo en la cabecera (header) en la versión móvil añadiendo la propiedad `overflow-hidden`.
- Se reparó el botón "Ver el PDF del menú" eliminando la intercepción por defecto (`e.preventDefault()`) y el retraso artificial, permitiendo que la carta en PDF abra correctamente en navegadores móviles sin ser bloqueada por los sistemas anti pop-up.
- Se subieron y sincronizaron los últimos cambios a los repositorios de GitHub (para actualización automática en Cloudflare) y GitLab (como respaldo).

## Archivos modificados
- `index.html`

## Problemas solucionados
- El logo del header sobresalía y tapaba el contenido inferior en la versión móvil.
- El botón de "Ver la Carta Completa" en PDF no abría el documento en teléfonos debido a la lógica del loader con retraso.

## Qué queda pendiente
- Nada. El proyecto está finalizado.
