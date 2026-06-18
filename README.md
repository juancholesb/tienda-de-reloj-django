# Tienda de Relojes - Django 5.2

Proyecto de tienda de venta de relojes desarrollado con Django 5.2.

## Requisitos

- Python  3.14.3
- pip

## Instalacion

1. Clonar el repositorio
2. Crear entorno virtual:
   python -m venv entorno
3. Activar entorno virtual:
   entorno\Scripts\activate
4. Instalar dependencias:
   pip install django==5.2

## Migraciones

python manage.py makemigrations
python manage.py migrate

## Crear superusuario

python manage.py createsuperuser  # se usará para acceder al admin

## Ejecutar servidor

python manage.py runserver 4000

## Acceso al admin

Ir a: http://127.0.0.1:4000/admin