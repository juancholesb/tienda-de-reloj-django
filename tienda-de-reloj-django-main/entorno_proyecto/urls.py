# URL configuration for entorno_proyecto project.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluir todas las rutas de la app; la app define la ruta raíz ('') como la vista de lista de productos.
    path('', include('apps.entorno_app.urls')),
]