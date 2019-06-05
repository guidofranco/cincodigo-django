Tener python 3.6.8 y django 2.2.1 instalados

Clonar el repo

cd cincodigo-django

python manage.py runserver

Para correr el test: python manage.py test

Procfile es un archivo que contiene los comandos que Heroku debe ejecutar para iniciar la aplicación

gunicorn es un servidor WSGI HTTP para python

Heroku reconoce el lenguaje de la aplicacion a ejecutar (y su versión) a partir del archivo runtime.txt y requirements.txt

Las modificaciones se hacen sobre el archivo myapp/views.py, aquí se crea una sola vista.

El test se define en myapp/tests.py, el cual se realiza sobre la vista anterior, verificando que exista un "Hello, world" en todo el contenido.