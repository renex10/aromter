# productos/models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()  # Cantidad en inventario
    descripcion = models.TextField()
    categoria = models.ForeignKey('categorias.Categoria', on_delete=models.CASCADE)
    proveedor = models.ForeignKey('proveedores.Proveedor', on_delete=models.CASCADE)
    formato = models.ForeignKey('formatos.Formato', on_delete=models.CASCADE)
    aroma = models.ForeignKey('aromas.Aroma', on_delete=models.CASCADE)
    ingrediente = models.ForeignKey('ingredientes.Ingrediente', on_delete=models.CASCADE)
    tipo = models.ForeignKey('tipo.Tipo', on_delete=models.CASCADE)
    grupo_etario = models.ForeignKey('grupo_etario.GrupoEtario', on_delete=models.CASCADE)
    producto_image = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

