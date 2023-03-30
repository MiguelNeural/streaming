# Streaming Neural10
## Iniciando un proyecto
- Instalar el entorno virtual pipenv:
`pipenv install django django-ckedit Pillow pylint pylint-django mysqlclient opencv-python`

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

## Desarrollo de aplicaciones
- Inicializar la aplicacion:
`python manage.py startapp <nombre_de_aplicacion>`
- Agregar la aplicacion a ***<nombre_del_proyecto>/settings.p***