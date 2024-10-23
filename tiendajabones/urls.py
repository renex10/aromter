# tiendajabones/urls.py
from django.contrib import admin
from django.urls import path
from productos.views import home, listar_productos
from categorias.views import listar_categorias  # Asegúrate de importar la vista

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('productos/', listar_productos, name='listar_productos'),
    path('categorias/', listar_categorias, name='listar_categorias'),  # Nueva ruta para categorías
]

# Esto sirve los archivos multimedia en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
