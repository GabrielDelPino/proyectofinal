# perfil/urls.py

from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('editar/', views.editar_perfil, name='editar_perfil'),  # Ruta para editar perfil
    path('detalle/', views.detalle_perfil, name='perfil_detalle'),  # Ruta para mostrar detalles del perfil
]



