from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from nuevo_evento.models import Evento
from agendar_cita.models import Cita
from perfil.models import Perfil
from .forms import NotificacionForm
from django.core.mail import EmailMessage
from django.utils.encoding import smart_str


def lista_notificaciones(request):
    perfil = Perfil.objects.get(usuario=request.user)
    eventos = Evento.objects.filter(usuario=request.user, asignado=True)
    citas = Cita.objects.filter(usuario=request.user)
    return render(request, 'notificaciones/lista_notificaciones.html', {
        'perfil': perfil,
        'eventos': eventos,
        'citas': citas,
    })


def enviar_notificacion(request):
    perfil = Perfil.objects.get(usuario=request.user)
    evento_id = request.GET.get('evento')
    cita_id = request.GET.get('cita')

    evento = get_object_or_404(Evento, id=evento_id) if evento_id else None
    cita = get_object_or_404(Cita, id=cita_id) if cita_id else None

    if request.method == 'POST':
        form = NotificacionForm(request.POST)
        if form.is_valid():
            notificacion = form.save(commit=False)
            notificacion.usuario = request.user
            notificacion.save()

            # Preparar el mensaje según el evento o la cita
            if evento:
                mensaje = f"""
                Detalles del evento:
                Título: {evento.titulo}
                Fecha: {evento.fecha}
                Hora: {evento.hora}
                Descripción: {evento.descripcion or 'Sin descripción'}
                """
            elif cita:
                mensaje = f"""
                Detalles de la cita:
                Cliente: {cita.cliente.nombre}
                Servicio: {cita.servicio.nombre}
                Fecha: {cita.fecha}
                Hora: {cita.hora}
                Notas: {cita.notas or 'Sin notas'}
                """
            else:
                mensaje = notificacion.mensaje

            # Intentar enviar el correo
            try:
                email = EmailMessage(
                    subject=smart_str('Notificación desde CalendarioPyme', encoding='utf-8'),
                    body=smart_str(mensaje, encoding='utf-8'),
                    from_email='tu_email@gmail.com',
                    to=[notificacion.destinatario]
                )
                email.send(fail_silently=False)
                notificacion.enviado = True
                notificacion.save()

                # Mensaje de éxito
                messages.success(request, 'La notificación se envió correctamente.')
                return redirect('lista_notificaciones')  # Redirigir a lista de notificaciones
            except Exception as e:
                # Mensaje de error
                messages.error(request, f"Error al enviar el correo: {e}")
    else:
        form = NotificacionForm()

    return render(request, 'notificaciones/enviar_notificacion.html', {
        'form': form,
        'perfil': perfil,
        'evento': evento,
        'cita': cita
    })





