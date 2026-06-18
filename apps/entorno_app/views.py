from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Reloj
from .forms import RelojForm

class ProductoListView(ListView):
    model = Reloj
    template_name = 'entorno_app/producto_list.html'
    context_object_name = 'object_list'

class ProductoCreateView(CreateView):
    model = Reloj
    form_class = RelojForm
    template_name = 'entorno_app/producto_form.html'
    success_url = reverse_lazy('producto-list')
