# Roadmap - Bar Luna Llena 16

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
- [x] **Rediseño Minimalista de Acordeón FAQ (21st.dev / shadcn):** Líneas divisorias sutiles, eliminación de tarjetas gruesas, chevron SVG rotatorio y plegado automático nativo (`name="faq-accordion"`).
- [x] **Mini Auditoría Automatizada con Playwright CLI:** Validación de 6 viewports (0 px de desbordamiento horizontal), 52 botones e interactividad 100% operativos y 0 errores JS en tiempo de ejecución.
- [x] **Sistema Tipográfico de Autor Fontshare:** Fusión armónica de **Clash Display** (H1 y H2), **Boska** (cita editorial de historia) y **Satoshi** (cuerpo, menús y legal), sustituyendo la antigua tipografía pesada en cursiva.
- [x] **Seguridad CSP Reforzada:** Autorización expresa en `_headers` de Cloudflare para Fontshare y Cloudflare Insights con 0 advertencias de seguridad en consola.

## Tareas en progreso
- [ ] Procesamiento en Google y motores de IA de la nueva Carta semántica HTML y Schemas de Santa Catalina.

## Próximas mejoras prioritarias
1. Solicitar re-indexación en Search Console con el `sitemap.xml` enriquecido.
2. Borrar o rotar la API key de Google que se pegó en el chat.
3. Conectar Search Console de forma automática (Cuenta de Servicio + archivo `.json` + script).
4. Valorar un dominio propio (ej. `barlunallena.com`) para consolidar la presencia de marca.
