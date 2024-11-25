from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('nuevo_evento', '0002_evento_asignado_alter_evento_fecha_alter_evento_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='usuario',
            field=models.ForeignKey(
                default=1,  # Cambia al ID de un usuario existente
                on_delete=models.CASCADE,
                related_name='eventos',
                to='auth.User',
            ),
        ),
    ]

