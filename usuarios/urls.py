# usuarios/urls.py

from django.urls import path
from .views import login_view, register_view  # Importa las vistas

urlpatterns = [
    path('login/', login_view, name='login'),  # Ruta para iniciar sesión
    path('register/', register_view, name='register'),  # Ruta para registrarse
]






