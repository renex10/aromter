from django.db import models

class Pedido(models.Model):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)  # Pendiente, Enviado, Entregado, etc.
    
    def __str__(self):
        return f'Pedido {self.id} de {self.cliente}'
