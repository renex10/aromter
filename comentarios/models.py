from django.db import models

class Comentario(models.Model):
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    texto = models.TextField()
    calificacion = models.PositiveIntegerField(default=5)  # Calificación del 1 al 5
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comentario de {self.cliente} sobre {self.producto}'

