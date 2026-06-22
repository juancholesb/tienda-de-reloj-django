from django.contrib import admin
from .models import (
    Marca, Categoria, Reloj, RelojCategoria,
    Cliente, PerfilCliente, Venta, DetalleVenta
)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais_origen']
    search_fields = ['nombre']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']


@admin.register(Reloj)
class RelojAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'marca', 'precio', 'stock', 'genero']
    list_filter = ['marca', 'genero']
    search_fields = ['modelo']


@admin.register(RelojCategoria)
class RelojCategoriaAdmin(admin.ModelAdmin):
    list_display = ['reloj', 'categoria']
    search_fields = ['reloj__modelo', 'categoria__nombre']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'telefono']
    search_fields = ['nombre', 'apellido', 'email']


@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'documento_identidad', 'fecha_nacimiento']
    search_fields = ['documento_identidad']


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha', 'total']
    list_filter = ['fecha']


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['venta', 'reloj', 'cantidad', 'precio_unitario']