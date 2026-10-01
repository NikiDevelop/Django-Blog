He creado un Blog con Django en donde tenemos varias secciones.

Lo primero que tienes que hacer es descargarte el proyecto.

Acto seguido vamos a descomprimir el proyecto, y lo abrimos con nuestro editor, en mi caso utilizo Visual Studio Code.

Creamos un entorno virtual.

```
$ python -m venv env
```
Tenemos que activar nuestro entorno virtual, tendremos que desplazarnos a la carpeta scripts.
```
$ cd env/scripts
```
Activamos nuestro entorno virtual.
```
$ .\activate
```
Ya tendríamos activado nuestro entorno virtual, debería salirte a la izquierda en color verde (env), eso quiere decir que está activado ya.

Ahora tenemos que regresar a nuestra carpeta del archivo, para eso utilizamos el siguiente comando por dos veces para regresar.

```
$ cd .. 
```

Ahora pasaremos a instalar las dependencias del proyecto.
```
$ pip install -r requirements.txt
```

Por último, ya solo te queda hacer las migraciones.
```
$ python manage.py makemigrations
```
```
$ python manage.py migrate
```
```
$ python manage.py runserver
```
No te olvides de crearte un usuario para poder administrar el blog. Rellena los datos que te pide, como nombre de usuario, 
el email lo puedes dejar en blanco si quieres dandole a enter y por último introduce una contraseña y repitela.
```
$ python manage.py createsuperuser
```

Cualquier sugerencia o participación que quieras aportar es bienvenida.

## Webs de tendencias

El proyecto incluye la app `nichos`, con **5 webs** creadas a partir de lo que más busca la gente en 2025-2026.
Cada web tiene su propio diseño, blog de artículos, comparativas con tabla y veredicto, radar de tendencias con
fuentes y una selección de productos con pros, contras y especificaciones.

| Web | Nicho | Por qué es tendencia |
|-----|-------|----------------------|
| 🤖 IA Fácil | Inteligencia artificial | «Cómo hacer fotos con IA» y «Gemini o ChatGPT», top de Google España 2025; generadores de voz IA +2.650 % |
| 🌿 Vida Longeva | Salud y longevidad | Boom de la creatina y la proteína; walking pad +4.300 %; «sleep coach» +93 % |
| 💶 Bolsillo Listo | Finanzas personales | «Amortizar plazo o cuota» y «Diésel o gasolina», top 2025; Euríbor al 2,855 % en julio de 2026 |
| ⚡ Casa Autónoma | Hogar, energía y preparación | «Apagón España», búsqueda nº 1 de 2025; el 56 % se plantea comprar un kit de emergencia |
| ✨ Piel y Estilo | Belleza y moda | Tónico PDRN +6.400 %; pantalones barrel leg +8.500 %; Labubu, top 10 en España |

Las fuentes de cada dato aparecen en la portada de cada web, en el apartado «Por qué esta web».

### Cargar las webs

Después de `migrate`, carga el contenido inicial (se puede repetir: actualiza sin duplicar):

```
$ python manage.py cargar_nichos
```

También puedes cargar solo algunas webs: `python manage.py cargar_nichos ia-facil casa-autonoma`.

### Dónde verlas

- `/webs/` — portada con las 5 webs
- `/webs/<web>/` — inicio de cada web (`ia-facil`, `vida-longeva`, `bolsillo-listo`, `casa-autonoma`, `piel-y-estilo`)
- `/webs/<web>/blog/`, `/comparativas/`, `/tendencias/`, `/productos/` y `/buscar/?q=`
- `/sitemap.xml` — mapa del sitio para buscadores

Todo el contenido se puede editar desde `/admin/` (Sitios, Artículos, Comparativas, Tendencias y Productos).
El texto inicial está en `nichos/contenido/`, un módulo por web.

### Antes de publicar

- Añade tus enlaces de afiliado en el campo «Enlace de compra o afiliado» de cada producto. Si está vacío, no se
  muestra el botón de compra.
- Revisa precios y especificaciones: son orientativos a octubre de 2026 y cambian a menudo.
- Las valoraciones de productos son editoriales, basadas en especificaciones. Si pruebas los productos, actualízalas.
- Para publicar cada web en su propio dominio, redirige la raíz de ese dominio a `/webs/<web>/` desde tu servidor web o proxy.

### Tests

```
$ python manage.py test nichos
```
