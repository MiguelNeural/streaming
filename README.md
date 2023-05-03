# Streaming Neural10
## Instalación
- Instalar el entorno virtual pipenv:

```Bash
pipenv install django django-ckedit Pillow pylint pylint-django mysqlclient opencv-python dj-static django-dbbackup openpyxl
```

> ##### Django-ckaedit
> Django CKEditor isntalla los JavaScript y funcionalidades para subir y explorar archivos en el servidor.
> #### Pillow
> Procesa imágenes. Soporta varios tipos de formatos de archivo.
> #### Pylint
> Pylint analiza el código sin ejecutarlo. Comprueba si hay errores, aplica un estándar de codificación, busca olores de código y puede hacer sugerencias sobre cómo refactorizar el código.
> #### OpenCV
> Libreria de visión computacional open source.
> #### MySQLClient
> Es una bifurcación de MySQL-python, que es una interfaz para el servidor de bases de datos MySQL.
> #### Dj-static
> Esta es una sencilla utilidad middleware de Django que te permite servir adecuadamente archivos estáticos desde producción con un servidor WSGI como Gunicorn.
> #### Django-dbbackup
> Esta aplicación Django proporciona comandos de gestión para ayudar a copia de seguridad y restaurar la base de datos del proyecto y archivos multimedia con varios almacenamientos como Amazon S3, DropBox o sistema de archivos local.
> #### Openpyxl
> Permite leer y escribir documentos de excel en formato .xslx

- Iniciar el entorno virtual:
`pipenv shell`

- Iniciar el proyecto de django:
`django-admin startprojec <nombre_del_proyecto>`

- Instalar paquetes necesarios para el motor de base de datos:
`pip install mysqlclient`

- Para actualizar cambios en la base de datos y configuraciones del proyecto:
`python manage.py migrate`
`python manage.py magemigrations`

- Se pueden crear bloques de codigo para facilitar el arranque del servidor:
```python
[scripts]
streaming =  "python streaming/manage.py runserver"
```
- Agregando el código anterior correremos los scripts creados con la siguiente linea de codigo:
`pipenv run <nombre_del_script>`

### settings.py
En el archivo settings.py se guardan configuraciones importantes para el funcionamiento del proyecto.
Para agregar las librerias hay que agregar el siguiente codigo.

#### 
````python
import os
import sys

LIBRARY_DIR = os.path.join(BASE_DIR, 'lib')
sys.path.append(LIBRARY_DIR)
```

## Desarrollo de aplicaciones
- Inicializar la aplicacion:
`python manage.py startapp <nombre_de_aplicacion>`
- Agregar la aplicacion a ***<nombre_del_proyecto>/settings.p***