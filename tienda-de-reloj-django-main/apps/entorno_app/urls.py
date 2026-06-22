from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
)

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto-create'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto-update'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto-delete'),
]