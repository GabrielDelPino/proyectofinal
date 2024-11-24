from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="eventos")  # Relación con el usuario
    titulo = models.CharField(max_length=100)
    fecha = models.DateField(blank=True, null=True)  # Permitir eventos sin fecha inicial
    hora = models.TimeField(blank=True, null=True)  # Permitir eventos sin hora inicial
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='eventos')
    descripcion = models.TextField(blank=True, null=True)
    recordatorio = models.BooleanField(default=False)
    asignado = models.BooleanField(default=False)  # Indicar si el evento está asignado al calendario

    def __str__(self):
        return self.titulo




