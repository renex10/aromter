from django.db import models

class Oferta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 20.00% de descuento
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    
    def __str__(self):
        return self.nombre

