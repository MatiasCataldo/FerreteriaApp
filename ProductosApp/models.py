from django.db import models

# Create your models here.
class Producto(models.Model):
    nombreProducto = models.CharField(max_length=20)
    idProducto = models.CharField(max_length=10)
    stock = models.CharField(max_length=8)
    fechaIngreso = models.DateField(null=True)
    productoImagen = models.ImageField(upload_to="productos", null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombreProducto} - {self.idProducto} - {self.stock} - {self.fechaIngreso} - {self.productoImagen}'