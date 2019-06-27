from django import forms
from .models import Paciente, Profesional
from datetime import datetime
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    
    class Meta():
        model = User
        fields = (
            'username',
            'email',
            )

        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nombre de usuario'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Requerido. 150 carácteres como máximo. Únicamente letras, dígitos y @/./+/-/_ '}),
            }

class PacienteForm(forms.ModelForm):
    
    class Meta:
        model = Paciente
        fields = (
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'run',
            'sexo',
            'fecha_nacimiento',
            'escolaridad',
            'ocupacion',
            'domicilio',
            'ciudad',
            'telefono',
            'prevision',
            'estado',
            #'user', #AGREGADO RECIENTEMENTE PARA PROBAR TEST
        )
            
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese nombre de paciente'}),
            'apellido_paterno' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese apellido paterno'}),
            'apellido_materno' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese apellido materno'}),
            'run' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese RUN de paciente'}),
            'sexo' : forms.RadioSelect(attrs={}),
            'fecha_nacimiento' : forms.DateInput(attrs={'class': 'form-control  pull-right', 'id' : 'datepicker'}),
            'escolaridad' : forms.Select(attrs={'class': 'form-control'}),
            'ocupacion' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Indique profesion u ocupación'}),
            'domicilio' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese domicilio de paciente'}),
            'ciudad' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese ciudad'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese N° de telefono', 'type' :'number'}),
            'prevision' : forms.Select(attrs={'class': 'form-control'}),
            'estado' : forms.Select(attrs={'class' : 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            self.paciente = kwargs.pop('paciente')   # the blog entry instance
            super().__init__(*args, **kwargs)

        def save(self):
            comment = super().save(commit=False)
            comment.paciente = self.user
            comment.save()
            return comment
