Tener python 3.6.8 y django 2.2.1 instalados

Clonar el repo

cd cincodigo-django

python manage.py collectstatic

python manage.py runserver

Para correr el test: python manage.py test

Procfile es un archivo que contiene los comandos que Heroku debe ejecutar para iniciar la aplicación

gunicorn es un servidor WSGI HTTP para python
Heroku conoce el lenguaje de la aplicacion a ejecutar (y su versión) a partir del archivo runtime.txt y requirements.txt