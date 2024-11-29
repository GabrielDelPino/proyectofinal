# nuevo_evento/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Crear categorías predeterminadas después de las migraciones
@receiver(post_migrate)
def crear_categorias_predeterminadas(sender, **kwargs):
    categorias_predeterminadas = ['Trabajo', 'Personal', 'Reunión']
    
    # Eliminar todas las categorías que no sean las predeterminadas
    Categoria.objects.exclude(nombre__in=categorias_predeterminadas).delete()
    
    # Crear las categorías predeterminadas si no existen
    for categoria in categorias_predeterminadas:
        Categoria.objects.get_or_create(nombre=categoria)

class Evento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="eventos")
    titulo = models.CharField(max_length=100)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='eventos')
    descripcion = models.TextField(blank=True, null=True)
    recordatorio = models.BooleanField(default=False)
    asignado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Nota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE, related_name='notas')
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nota para {self.evento.titulo} - {self.texto[:20]}"







