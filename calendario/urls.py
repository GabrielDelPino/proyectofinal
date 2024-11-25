# calendario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendario'),  # Ruta principal para el calendario
]

