from django import forms

class CreacionProducto(forms.Form):
    nombreProducto = forms.CharField(max_length=20)
    idProducto = forms.CharField(max_length=20)
    stock = forms.CharField(max_length=8)
    fechaIngreso = forms.DateField(widget=forms.SelectDateWidget(years=range(2020, 2026)))
