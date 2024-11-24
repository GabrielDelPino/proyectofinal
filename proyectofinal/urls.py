"""
URL configuration for proyectofinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# proyectofinal/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('', lambda request: redirect('usuarios:login')),
    path('perfil/', include('perfil.urls')),
    path('calendario/', include('calendario.urls')),
    path('nuevo_evento/', include('nuevo_evento.urls')),
    path('agendar_cita/', include('agendar_cita.urls')),
    path('notificaciones/', include('notificaciones.urls')),  # Correctamente registrado
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










