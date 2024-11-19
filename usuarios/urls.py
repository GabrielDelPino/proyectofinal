# usuarios/urls.py
from django.urls import path
from . import views

app_name = 'usuarios'  # Namespace para esta aplicación

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Ruta para el login
    path('register/', views.register_view, name='register'),  # Ruta para el registro
]












