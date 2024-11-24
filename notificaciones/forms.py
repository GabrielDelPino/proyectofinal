from django import forms
from .models import Notificacion

class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields = ['evento', 'cita', 'destinatario', 'mensaje']
        widgets = {
            'destinatario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo o WhatsApp'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
