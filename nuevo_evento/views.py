from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm
from perfil.models import Perfil  # Importa el modelo de Perfil

def nuevo_evento(request):
    perfil = Perfil.objects.get(usuario=request.user)  # Obtén el perfil del usuario
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.usuario = request.user  # Asocia el evento al usuario autenticado
            evento.asignado = False  # Inicialmente no asignado
            evento.save()
            return redirect('asignar_evento', evento_id=evento.id)  # Redirige a la asignación
    else:
        form = EventoForm()
    return render(request, 'nuevo_evento/nuevo_evento.html', {'form': form, 'perfil': perfil})

def asignar_evento(request, evento_id):
    perfil = Perfil.objects.get(usuario=request.user)  # Obtén el perfil del usuario
    evento = get_object_or_404(Evento, id=evento_id, usuario=request.user)  # Filtra el evento por usuario
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        if fecha and hora:
            evento.fecha = fecha
            evento.hora = hora
            evento.asignado = True
            evento.save()
            return redirect('calendario')  # Redirige al calendario
    return render(request, 'nuevo_evento/asignar_evento.html', {'evento': evento, 'perfil': perfil})











