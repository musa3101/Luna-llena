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
- [x] **Auditoría Integral de Rendimiento y Código Muerto:** Corrección del enlace roto `#historia` ➔ `#origen`, purga de ~38 KB de código muerto (antiguos modales legal, reservas y FAB huérfanos), limpieza de selectores Swiper y verificación al 100% de los 15 botones activos.
- [x] **Optimización Extrema de Rendimiento y Assets:** WebP en todos los medios, favicons optimizados, eliminación de assets obsoletos, dependencias Swiper locales (0 CDN), alcanzando **94 en Móvil y 98 en Desktop** en Google Lighthouse con 0 ms TBT.
- [x] **Indexación Avanzada para IAs & Buscadores:** Directivas en `robots.txt` para GPTBot, PerplexityBot, ClaudeBot, etc. Schemas completos `Menu` (28 platos con precios) y `FAQPage` geolocalizado en Santa Catalina.
- [x] **Carta HTML Desplegable en Marfil Crema Bistró:** Botón compacto bajo la carta (`VER CARTA EN DETALLE ▾`), contenedor marfil cálido (`#FAF7F2`) con lista a 2 columnas desktop / 1 móvil, puntos guía, precios dorados y 2 botones de acción (*Cerrar Carta* y *Reservar Mesa en Bavoli*).
- [x] **Rediseño Moderno de Acordeón FAQ:** Lenguaje 100% natural sin tecnicismos, integración de FAQ oficial de Reservas y Cancelaciones con Bavoli, tarjetas translúcidas con bordes dorados y chevrons SVG rotatorios.
- [x] **Validación Responsive Automatizada:** Auditoría en 6 viewports con Playwright demostrando 0 desbordamiento horizontal y 0 errores en consola.

## Tareas en progreso
- [ ] Procesamiento en Google y motores de IA de la nueva Carta semántica HTML y Schemas de Santa Catalina.

## Próximas mejoras prioritarias
1. Solicitar re-indexación en Search Console con el `sitemap.xml` enriquecido.
2. Borrar o rotar la API key de Google que se pegó en el chat.
3. Conectar Search Console de forma automática (Cuenta de Servicio + archivo `.json` + script).
4. Valorar un dominio propio (ej. `barlunallena.com`) para consolidar la presencia de marca.
