from django.urls import path
from . import views

urlpatterns = [
    path('', views.nuevo_evento, name='nuevo_evento'),  # Ruta para crear un evento
    path('asignar/<int:evento_id>/', views.asignar_evento, name='asignar_evento'),  # Ruta para asignar el evento
]






