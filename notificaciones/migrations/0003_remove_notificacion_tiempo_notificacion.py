# Generated by Django 5.1.3 on 2024-11-25 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notificaciones', '0002_notificacion_tiempo_notificacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacion',
            name='tiempo_notificacion',
        ),
    ]