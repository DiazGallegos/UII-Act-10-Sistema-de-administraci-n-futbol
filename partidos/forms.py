from django import forms
from .models import Partido

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = '__all__'
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'equipo_local': forms.TextInput(attrs={'class': 'form-control'}),
            'equipo_visitante': forms.TextInput(attrs={'class': 'form-control'}),
            'estadio': forms.TextInput(attrs={'class': 'form-control'}),
            'goles_local': forms.NumberInput(attrs={'class': 'form-control'}),
            'goles_visitante': forms.NumberInput(attrs={'class': 'form-control'}),
        }