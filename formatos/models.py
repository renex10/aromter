from django.db import models

class Formato(models.Model):
    nombre = models.CharField(max_length=100)  # Ejemplo: Botella, Barra, etc.
    tamanio = models.CharField(max_length=50)  # Ejemplo: 500ml, 200g, etc.

    def __str__(self):
        return f'{self.nombre} ({self.tamanio})'

