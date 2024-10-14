from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirigir después de iniciar sesión (cambia 'home' según tu ruta)
        else:
            # Mostrar mensaje de error si las credenciales son incorrectas
            return render(request, 'usuarios/login.html', {'error': 'Correo o contraseña incorrectos'})
    return render(request, 'usuarios/login.html')

