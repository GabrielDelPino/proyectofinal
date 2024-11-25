from django.urls import path
from . import views

urlpatterns = [
    path('', views.nuevo_evento, name='nuevo_evento'),
    path('asignar/<int:evento_id>/', views.asignar_evento, name='asignar_evento'),
    path('lista-eventos/', views.lista_eventos, name='lista_eventos'),
    path('detalle-evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('eliminar-nota/<int:nota_id>/', views.eliminar_nota, name='eliminar_nota'),
]









