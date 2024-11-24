from django.db import models
from django.contrib.auth.models import User
from nuevo_evento.models import Evento
from agendar_cita.models import Cita

class Notificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, null=True, blank=True)
    destinatario = models.CharField(max_length=15)  # Para almacenar el número o email
    mensaje = models.TextField()
    enviado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificación para {self.destinatario} ({'Enviado' if self.enviado else 'Pendiente'})"
