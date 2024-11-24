from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm

def nuevo_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.asignado = False  # Inicialmente no asignado
            evento.save()
            return redirect('asignar_evento', evento_id=evento.id)  # Redirige a la asignación
    else:
        form = EventoForm()
    return render(request, 'nuevo_evento/nuevo_evento.html', {'form': form})

def asignar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        if fecha and hora:
            evento.fecha = fecha
            evento.hora = hora
            evento.asignado = True
            evento.save()
            return redirect('calendario')  # Redirige al calendario
    return render(request, 'nuevo_evento/asignar_evento.html', {'evento': evento})









