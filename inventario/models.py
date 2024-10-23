from django.db import models

class Inventario(models.Model):
    producto = models.OneToOneField('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad} en inventario'

