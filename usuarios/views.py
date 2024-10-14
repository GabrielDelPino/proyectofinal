# usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    return render(request, 'usuarios/login.html')  # Cargar la plantilla de inicio de sesión

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Crear un nuevo usuario
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Cuenta creada con éxito.')
        return redirect('login')  # Redirige al inicio de sesión después de registrarse

    return render(request, 'usuarios/register.html')  # Cargar la plantilla de registro



