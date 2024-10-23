from django.db import models

class Tipo(models.Model):
    nombre = models.CharField(max_length=100)  # Ejemplo: Líquido, Sólido, etc.

    def __str__(self):
        return self.nombre

