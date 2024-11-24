from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notificaciones, name='lista_notificaciones'),
    path('enviar/', views.enviar_notificacion, name='enviar_notificacion'),
]



