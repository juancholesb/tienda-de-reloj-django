from django.urls import path
from .views import ProductoListView, ProductoCreateView

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto-create'),
]
