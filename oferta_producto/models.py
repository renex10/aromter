from django.db import models

from django.db import models
from productos.models import Producto
from ofertas.models import Oferta

class OfertaProducto(models.Model):
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.producto.nombre} - {self.oferta.nombre}'

