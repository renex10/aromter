# categorias/models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    categoria_image = models.ImageField(upload_to='categorias/', blank=True, null=True)

    def __str__(self):
        return self.nombre


