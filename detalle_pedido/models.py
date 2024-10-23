from django.db import models

class DetallePedido(models.Model):
    pedido = models.ForeignKey('pedidos.Pedido', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'

