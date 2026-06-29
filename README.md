# Bar Cafetería Luna Llena 🌙

Sitio web oficial bilingüe (Español / Inglés) del **Bar Cafetería Luna Llena**, ubicado en Santa Catalina, Palma de Mallorca. 

Este proyecto está optimizado con enfoque Mobile-First, cuenta con carga de contenidos dinámicos desde Supabase, optimización agresiva de imágenes y un diseño visual premium adaptado a dispositivos móviles.

---

## 🚀 Características Clave

* **Soporte Bilingüe Completo (ES/EN):** Traducción instantánea integrada en JavaScript (en caliente) para todo el sitio web.
* **Apertura de PDF Limpia:** Enlace del menú digital optimizado para cargar páginas específicas (español o inglés) sin controles laterales del navegador.
* **Backend de Supabase:** Estructura preparada para el almacenamiento de traducciones dinámicas y platos directamente desde base de datos con fallback local.
* **Optimización de Rendimiento:** Reducción de más de 7.5 MB en imágenes mediante compresión programática para asegurar una carga ultrarrápida.
* **Diseño Premium Responsivo:** UI y efectos fluidos con Outfit y Playfair Display en todas las pantallas.

---

## 🛠️ Tecnologías y Recursos

* **Frontend:** HTML5, CSS3, Tailwind CSS (utilidades compiladas), Javascript ES6.
* **Librerías:** Swiper JS (Carrusel interactivo de historia 3D Coverflow).
* **Base de Datos:** Supabase JS Client (CDN).
* **Servidor de Producción / Despliegue:** Cloudflare Pages integrado directamente con GitHub/GitLab.

---

## 🗄️ Configuración de Supabase (Base de Datos)

Para activar el control dinámico del contenido de la web, sigue estos pasos:

1. Importa el archivo SQL de la base de datos ubicado en:  
   `docs/supabase_schema.sql` en la consola SQL de tu proyecto en Supabase.
2. Esto creará las tablas `site_content` y `dishes` y poblará los textos bilingües de la semilla.
3. Rellena los datos de conexión correspondientes en la sección inferior de `index.html`:
   ```javascript
   const SUPABASE_URL = "TU_SUPABASE_URL";
   const SUPABASE_ANON_KEY = "TU_SUPABASE_ANON_KEY";
   ```
4. El cargador dinámico reemplazará automáticamente todos los textos sin necesidad de modificar el código.

---

## 👨‍💻 Créditos
Desarrollado y respaldado tecnológicamente por **MYNEXT**.
