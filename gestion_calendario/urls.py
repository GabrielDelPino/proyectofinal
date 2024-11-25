from django.urls import path
from . import views

app_name = 'gestion_calendario'

urlpatterns = [
    path('', views.listar_eventos_citas, name='listar_eventos_citas'),
    path('eliminar_evento/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    path('eliminar_cita/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
]



