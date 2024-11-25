from django import forms
from .models import Notificacion

class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields = ['evento', 'cita', 'destinatario', 'mensaje']
        widgets = {
            'destinatario': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo del destinatario'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'evento': forms.Select(attrs={'class': 'form-control'}),
            'cita': forms.Select(attrs={'class': 'form-control'}),
        }

