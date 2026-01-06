from django import forms
from .models import Horario

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['docente', 'disciplina', 'ano', 'dia', 'inicio', 'fim']
        widgets = {
            'docente': forms.TextInput(attrs={'class': 'form-control'}),
            'disciplina': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'dia': forms.Select(attrs={'class': 'form-select'}),
            'inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'fim': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
