from django.shortcuts import render, redirect
from .models import Cita, Servicio, Cliente
from .forms import CitaForm, ServicioForm, ClienteForm
from perfil.models import Perfil

def agendar_cita(request):
    perfil = Perfil.objects.get(usuario=request.user)
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.usuario = request.user
            cita.save()
            return redirect('lista_citas')  # Redirige a la lista de citas
    else:
        form = CitaForm()
    return render(request, 'agendar_cita/agendar_cita.html', {'form': form, 'perfil': perfil})


def lista_citas(request):
    perfil = Perfil.objects.get(usuario=request.user)
    citas = Cita.objects.filter(usuario=request.user).order_by('fecha', 'hora')
    return render(request, 'agendar_cita/lista_citas.html', {'citas': citas, 'perfil': perfil})


def crear_servicio(request):
    perfil = Perfil.objects.get(usuario=request.user)
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendar_cita')  # Redirige de nuevo a agendar cita
    else:
        form = ServicioForm()
    return render(request, 'agendar_cita/crear_servicio.html', {'form': form, 'perfil': perfil})


def crear_cliente(request):
    perfil = Perfil.objects.get(usuario=request.user)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendar_cita')  # Redirige de nuevo a agendar cita
    else:
        form = ClienteForm()
    return render(request, 'agendar_cita/crear_cliente.html', {'form': form, 'perfil': perfil})
