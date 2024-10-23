from django.db import models

class Aroma(models.Model):
    nombre = models.CharField(max_length=100)  # Ejemplo: Lavanda, Vainilla, etc.

    def __str__(self):
        return self.nombre

