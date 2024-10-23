

# categorias/views.py
from django.shortcuts import render
from .models import Categoria

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista_categorias.html', {'categorias': categorias})

