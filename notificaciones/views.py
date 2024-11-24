from django.shortcuts import render, redirect
from nuevo_evento.models import Evento
from agendar_cita.models import Cita
from perfil.models import Perfil
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
    if request.method == 'POST':
        destinatario = request.POST.get('destinatario')
        asunto = request.POST.get('asunto', 'Notificación desde CalendarioPyme')
        mensaje = request.POST.get('mensaje', 'Detalle de la notificación.')

        try:
            email = EmailMessage(
                subject=smart_str(asunto, encoding='utf-8'),
                body=smart_str(mensaje, encoding='utf-8'),
                from_email='tu_email@gmail.com',  # Cambia al correo configurado
                to=[destinatario]
            )
            email.send(fail_silently=False)
            return redirect('lista_notificaciones')  # Asegúrate de que coincida con el nombre en urls.py
        except Exception as e:
            return render(request, 'notificaciones/enviar_notificacion.html', {
                'error': f"Error al enviar el correo: {e}",
                'perfil': perfil,
            })

    return render(request, 'notificaciones/enviar_notificacion.html', {'perfil': perfil})


