from django import forms
from .models import Reloj

class RelojForm(forms.ModelForm):
    class Meta:
        model = Reloj
        fields = ['marca', 'modelo', 'precio', 'stock', 'genero', 'descripcion', 'imagen_url']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
