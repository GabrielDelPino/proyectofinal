from django.db import models
from django.contrib.auth.models import User

class Cita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=255)
    servicio = models.CharField(max_length=255)
    fecha = models.DateTimeField()  # Campo correcto para fecha y hora

    def __str__(self):
        return f"{self.cliente} - {self.servicio} - {self.fecha}"


