from django.shortcuts import render, get_object_or_404, redirect
from nuevo_evento.models import Evento
from agendar_cita.models import Cita
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from perfil.models import Perfil

@login_required
def listar_eventos_citas(request):
    perfil = Perfil.objects.get(usuario=request.user)  # Obtén el perfil del usuario
    eventos = Evento.objects.filter(usuario=request.user)
    citas = Cita.objects.filter(usuario=request.user)
    return render(request, 'gestion_calendario/listar.html', {
        'perfil': perfil,
        'eventos': eventos,
        'citas': citas,
    })


def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id, usuario=request.user)
    evento.delete()
    return redirect('gestion_calendario:listar_eventos_citas')


def eliminar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id, usuario=request.user)
    cita.delete()
    return redirect('gestion_calendario:listar_eventos_citas')

