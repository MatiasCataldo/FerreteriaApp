from django import forms

class CreacionSocio(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.CharField(max_length=8)
    direccion = forms.CharField(max_length=20)
    celular = forms.CharField(max_length=20)