from django.db import models

class GrupoEtario(models.Model):
    nombre = models.CharField(max_length=100)  # Ejemplo: Adultos, Niños, etc.
    
    def __str__(self):
        return self.nombre
