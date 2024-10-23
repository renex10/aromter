# productos/views.py
from django.shortcuts import render
from .models import Producto  # Asegúrate de importar tu modelo Producto

def home(request):
    return render(request, 'home.html')  # Esto asume que home.html está en templates/

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_producto.html', {'productos': productos})  # Esto asume que lista_producto.html está en templates/productos/


