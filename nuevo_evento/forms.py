from django import forms
from .models import Evento, Categoria, Nota

class EventoForm(forms.ModelForm):
    nueva_categoria = forms.CharField(
        required=False,
        label="Nueva Categoría",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Crear nueva categoría'}),
    )

    class Meta:
        model = Evento
        fields = ['titulo', 'categoria', 'descripcion', 'recordatorio']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Evento'}),
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

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nota aquí'}),
        }



