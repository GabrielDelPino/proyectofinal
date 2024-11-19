# usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Inicia sesión al usuario
            return redirect('perfil:editar_perfil')  # Redirige a la página de edición de perfil
        else:
            messages.error(request, 'Credenciales incorrectas')
    return render(request, 'usuarios/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verificar si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('usuarios:register')

        # Verificar si el correo electrónico ya está registrado
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
            return redirect('usuarios:register')

        # Crear un nuevo usuario
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Cuenta creada con éxito.')
        return redirect('usuarios:login')  # Redirige al inicio de sesión después de registrarse

    return render(request, 'usuarios/register.html')