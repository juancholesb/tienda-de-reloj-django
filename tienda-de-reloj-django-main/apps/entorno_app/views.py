from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from .models import Reloj, Cliente, Venta, DetalleVenta


class ProductoListView(ListView):
    """Vista pública: solo LECTURA del catálogo de relojes."""
    model = Reloj
    template_name = 'entorno_app/producto_list.html'
    context_object_name = 'relojes'


# =============================================================
# CARRITO DE COMPRAS (usando sesiones de Django)
# =============================================================

def agregar_al_carrito(request, pk):
    """Agrega un reloj al carrito (sesión)."""
    reloj = get_object_or_404(Reloj, pk=pk)
    carrito = request.session.get('carrito', {})

    reloj_id = str(pk)
    if reloj_id in carrito:
        carrito[reloj_id]['cantidad'] += 1
    else:
        carrito[reloj_id] = {
            'nombre': f"{reloj.marca.nombre} {reloj.modelo}",
            'precio': str(reloj.precio),
            'cantidad': 1,
            'imagen_url': reloj.imagen_url or '',
        }

    request.session['carrito'] = carrito
    messages.success(request, f'"{reloj.modelo}" agregado al carrito.')
    return redirect('producto-list')


def ver_carrito(request):
    """Muestra el contenido del carrito."""
    carrito = request.session.get('carrito', {})
    items = []
    total = 0

    for reloj_id, datos in carrito.items():
        subtotal = float(datos['precio']) * datos['cantidad']
        total += subtotal
        items.append({
            'id': reloj_id,
            'nombre': datos['nombre'],
            'precio': float(datos['precio']),
            'cantidad': datos['cantidad'],
            'subtotal': subtotal,
            'imagen_url': datos.get('imagen_url', ''),
        })

    return render(request, 'entorno_app/carrito.html', {
        'items': items,
        'total': total,
    })


def eliminar_del_carrito(request, pk):
    """Elimina un producto del carrito."""
    carrito = request.session.get('carrito', {})
    reloj_id = str(pk)

    if reloj_id in carrito:
        del carrito[reloj_id]
        request.session['carrito'] = carrito
        messages.info(request, 'Producto eliminado del carrito.')

    return redirect('ver-carrito')


def checkout(request):
    """Formulario de compra: nombre, datos y dirección de envío."""
    carrito = request.session.get('carrito', {})

    if not carrito:
        messages.warning(request, 'Tu carrito está vacío.')
        return redirect('producto-list')

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        email = request.POST.get('email', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        direccion = request.POST.get('direccion', '').strip()

        # Validación básica
        if not nombre or not apellido or not email or not direccion:
            messages.error(request, 'Por favor completa todos los campos obligatorios.')
            return render(request, 'entorno_app/checkout.html', {
                'carrito': carrito,
            })

        # Crear o buscar el cliente
        cliente, created = Cliente.objects.get_or_create(
            email=email,
            defaults={
                'nombre': nombre,
                'apellido': apellido,
                'telefono': telefono,
                'direccion': direccion,
            }
        )

        # Calcular total
        total = 0
        for datos in carrito.values():
            total += float(datos['precio']) * datos['cantidad']

        # Crear la venta
        venta = Venta.objects.create(
            cliente=cliente,
            total=total,
        )

        # Crear los detalles de la venta
        for reloj_id, datos in carrito.items():
            reloj = Reloj.objects.get(pk=int(reloj_id))
            DetalleVenta.objects.create(
                venta=venta,
                reloj=reloj,
                cantidad=datos['cantidad'],
                precio_unitario=reloj.precio,
            )
            # Descontar stock
            reloj.stock -= datos['cantidad']
            reloj.save()

        # Vaciar el carrito
        request.session['carrito'] = {}

        return render(request, 'entorno_app/compra_exitosa.html', {
            'venta': venta,
            'cliente': cliente,
        })

    # GET: mostrar formulario
    items = []
    total = 0
    for reloj_id, datos in carrito.items():
        subtotal = float(datos['precio']) * datos['cantidad']
        total += subtotal
        items.append({
            'nombre': datos['nombre'],
            'precio': float(datos['precio']),
            'cantidad': datos['cantidad'],
            'subtotal': subtotal,
        })

    return render(request, 'entorno_app/checkout.html', {
        'items': items,
        'total': total,
    })