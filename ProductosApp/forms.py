from django import forms
from .models import Producto

class CreacionProducto(forms.Form):
    nombreProducto = forms.CharField(max_length=20)
    idProducto = forms.CharField(max_length=20)
    stock = forms.CharField(max_length=8)
    fechaIngreso = forms.DateField(widget=forms.SelectDateWidget(years=range(2020, 2026)))
    productoImagen = forms.ImageField(required=False, label="Imagen del Producto")

    class Meta:
        model = Producto
        fields = ['nombreProducto', 'idProducto', 'stock', 'fechaIngreso', 'productoImagen']
        widgets = {
            'fechaIngreso': forms.SelectDateWidget(years=range(2020, 2026))
        }
        labels = {
            'productoImagen': 'Imagen del Producto'
        }