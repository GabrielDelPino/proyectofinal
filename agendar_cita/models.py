from django.db import models
from django.contrib.auth.models import User

class Servicio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citas')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cliente} - {self.servicio} ({self.fecha} {self.hora})"

