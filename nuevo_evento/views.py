from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Nota
from .forms import EventoForm, NotaForm
from perfil.models import Perfil

def nuevo_evento(request):
    perfil = Perfil.objects.get(usuario=request.user)
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.usuario = request.user
            evento.asignado = False
            evento.save()
            return redirect('asignar_evento', evento_id=evento.id)
    else:
        form = EventoForm()
    return render(request, 'nuevo_evento/nuevo_evento.html', {'form': form, 'perfil': perfil})


def asignar_evento(request, evento_id):
    perfil = Perfil.objects.get(usuario=request.user)
    evento = get_object_or_404(Evento, id=evento_id, usuario=request.user)
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        if fecha and hora:
            evento.fecha = fecha
            evento.hora = hora
            evento.asignado = True
            evento.save()
            return redirect('calendario')
    return render(request, 'nuevo_evento/asignar_evento.html', {'evento': evento, 'perfil': perfil})


def lista_eventos(request):
    perfil = Perfil.objects.get(usuario=request.user)
    eventos = Evento.objects.filter(usuario=request.user, asignado=True)
    return render(request, 'nuevo_evento/lista_eventos.html', {'eventos': eventos, 'perfil': perfil})


def detalle_evento(request, evento_id):
    perfil = Perfil.objects.get(usuario=request.user)
    evento = get_object_or_404(Evento, id=evento_id, usuario=request.user)
    notas = evento.notas.all()
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.evento = evento
            nota.usuario = request.user
            nota.save()
            return redirect('detalle_evento', evento_id=evento.id)
    else:
        form = NotaForm()
    return render(request, 'nuevo_evento/detalle_evento.html', {'evento': evento, 'notas': notas, 'form': form, 'perfil': perfil})


def eliminar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id, usuario=request.user)
    evento_id = nota.evento.id
    nota.delete()
    return redirect('detalle_evento', evento_id=evento_id)













