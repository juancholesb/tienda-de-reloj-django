from django.urls import path
from .views import (
    ProductoListView,
    agregar_al_carrito,
    ver_carrito,
    eliminar_del_carrito,
    checkout,
)

urlpatterns = [
    # Volvemos a poner el catálogo en 'productos/'
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    
    # Rutas del carrito
    path('carrito/', ver_carrito, name='ver-carrito'),
    path('carrito/agregar/<int:pk>/', agregar_al_carrito, name='agregar-carrito'),
    path('carrito/eliminar/<int:pk>/', eliminar_del_carrito, name='eliminar-carrito'),
    path('checkout/', checkout, name='checkout'),
]