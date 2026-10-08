# Roadmap - Bar Luna Llena

## Tareas completadas
- [x] Web completa en producción (Cloudflare Pages) con carrusel, carta interactiva ES/EN, reservas por WhatsApp, textos legales y Supabase.
- [x] Optimización de imágenes, animaciones del logo, separadores Bangladesh y navegación suave.
- [x] Auditoría de seguridad y limpieza del proyecto.
- [x] QR físico de mesas redirigido a la carta interactiva (`_redirects`), sin reimprimir.
- [x] Rutas `/menu` y `/carta` + botón "Atrás" del móvil en el visor de carta.
- [x] Verificación de Google Search Console y `sitemap.xml` actualizado.
- [x] `manifest.json`, datos estructurados `WebSite` y suite de favicons para que Google muestre "Bar Luna Llena 16".
- [x] **Auditoría completa de SEO & Geo SEO:** Corrección canónica del sitemap, Geo meta tags (Palma / Santa Catalina), Schema `BarOrPub` enriquecido con menú, reservas y pagos, jerarquía H1 y optimización de OpenGraph.
- [x] **Auditoría de Tests, Código y Seguridad:** Eliminación de script Supabase duplicado, sanitización y encoding RFC 3986 en WhatsApp URLs, cabeceras HTTP de seguridad (`_headers` para Cloudflare Pages) y saneamiento de secretos en workflows CI/CD.

## Tareas en progreso
- [ ] Procesamiento en Google de los nuevos datos estructurados, Geo tags y nombre del sitio ("Bar Luna Llena 16").

## Próximas mejoras prioritarias
1. Solicitar re-indexación en Search Console con el `sitemap.xml` limpio.
2. Borrar o rotar la API key de Google que se pegó en el chat.
3. Conectar Search Console de forma automática (Cuenta de Servicio + archivo `.json` + script).
4. Valorar un dominio propio (ej. `barlunallena.com`) para consolidar la presencia de marca.

