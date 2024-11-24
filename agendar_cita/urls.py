from django.urls import path
from . import views

urlpatterns = [
    path('', views.agendar_cita, name='agendar_cita'),  # Página para agendar citas
    path('lista/', views.lista_citas, name='lista_citas'),  # Página para listar citas
    path('crear-servicio/', views.crear_servicio, name='crear_servicio'),  # Página para crear servicios
    path('crear-cliente/', views.crear_cliente, name='crear_cliente'),  # Página para crear clientes
]

