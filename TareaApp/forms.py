#from django.forms import ModelForm
from .models import Tarea
from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_limite', 'asignado_a', 'archivo_adjunto', 'importante']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo de la tarea.'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder': 'Describe la tarea.'}),
            'fecha_limite': forms.TextInput(attrs={'type': 'datetime-local'}),
            'importante': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }
