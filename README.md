Este proyecto consiste en una aplicación básica de un blog, basada en el [tutorial de CodeSwallow](https://www.youtube.com/playlist?list=PLGUsAPwPODljydJyw2ptMwoPdbpVzyjQe), cuyo repositorio es [este](https://github.com/CodeSwallow/django-blog). Con el mismo se pueden probar y practicar muchas cuestiones básicas de un proyecto de este tipo con Django.

# Cómo correr este proyecto

- Descargar este repositorio (se puede hacer desde la terminal ubicandose en la carpeta deseada y escribiendo `git clone https://github.com/devsiderio/devsiderio-blog`)

- Luego, en sistemas operativos basados en Debian/Ubuntu, ejecutar los siguientes comandos para instalar pip y pipenv:
  
``sudo apt install python3-pip
pip install pipenv``

- Posicionarse desde la terminal sobre la carpeta del proyecto.

- Ejecutar los siguientes comandos:
  
``pipenv install
pipenv shell
pipenv install django
pipenv install markdown pillow django-crispy-forms crispy-bootstrap5
python3 manage.py createsuperuser
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver``

(A la hora de crear un superuser puede ser, por ejemplo, usuario: admin, contraseña: 1234)

- Para publicar nuevos posts y administrar el sitio en general, acceder desde http://127.0.0.1:8000/admin/ con las credenciales de administrador (admin, 1234).

- Al hacer cambios en la base de datos, bajar el servidor (Ctrl+C) y volver a correr:

``python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver``