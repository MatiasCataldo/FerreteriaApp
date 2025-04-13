from django.db import models

# Create your models here.
class Socio(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=8)
    direccion = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.dni} - {self.direccion} - {self.celular}'