from django.forms import ModelForm
from .models import Tarea


from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_limite', 'asignado_a', 'archivo_adjunto']
        widgets = {
            'fecha_limite': forms.TextInput(attrs={'type': 'datetime-local'}),
        }
