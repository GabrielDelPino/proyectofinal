from django import forms
from .models import Evento, Categoria

class EventoForm(forms.ModelForm):
    nueva_categoria = forms.CharField(
        required=False,
        label="Nueva Categoría",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Crear nueva categoría'}),
    )

    class Meta:
        model = Evento
        fields = ['titulo', 'fecha', 'hora', 'categoria', 'descripcion', 'recordatorio']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Evento'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción'}),
            'recordatorio': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def save(self, commit=True):
        nueva_categoria = self.cleaned_data.get('nueva_categoria')
        if nueva_categoria:
            categoria, created = Categoria.objects.get_or_create(nombre=nueva_categoria)
            self.instance.categoria = categoria
        return super().save(commit)


