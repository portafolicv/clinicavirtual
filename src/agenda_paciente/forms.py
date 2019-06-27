from django import forms
from .models import ControlMedico, Minuta_Paciente
from datetime import datetime


class ControlMedicoForm(forms.ModelForm):
    class Meta():
        model = ControlMedico
        fields = {
            'fechaControl',
            'horaControl',
            'asiste',
            'paciente'
        }
        widgets = {
            'fechaControl' : forms.DateInput(attrs={'class': 'form-control  pull-right', 'id' : 'datepicker'}),
            'horaControl' : forms.TimeInput(attrs={'class': 'form-control  pull-right'}),
            'asiste': forms.CheckboxInput(attrs={'class' : 'form-control'}),
            'paciente': forms.Select(attrs={'class' : 'form-control'}),
        }


class MinutaPacienteForm(forms.ModelForm):
    class Meta():
        model = Minuta_Paciente
        fields = {
            'minuta',
            'observaciones',
        }
        widgets = {
            'minuta': forms.Select(attrs={'class' : 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class' : 'form-control'}),
        }