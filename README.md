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
Ya tendriamos antivado nuestro entorno virtual, debería salirte a la izquiera en color verde (env), eso quiere decir que esta activado ya.

Ahora tenemos que regresar a nuestra carpeta del archivo para eso utilizamos el siguiente comando por dos veces para regresar.

```
$ cd .. 
```

Genial! ya podemos instalar Django con sus dependencias del proyecto.
```
$ pip install -r requirements.txt
```

Por último ya solo te queda hacer las migraciones.
```
$ python manage.py makemigrations
```
```
$ python manage.py migarate
```
```
$ python manage.py runserver
```
No te olvides de crearte un usuario para poder administrar el blog. Rellena los datos que te pide, como nombre de usuario, 
el email lo puedes dejar en blanco si quieres dandole a enter y por último introduce una contraseña y repitela.
```
$ python manage.py createsuperuser
```

Este proyecto se puede escalar como quieras.
Cualquier sugerencia o participación que quieras aportar es bienvenida.
