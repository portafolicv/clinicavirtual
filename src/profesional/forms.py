from django import forms
from .models import Profesional
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = (
            'username',
            #'password',
            'email',
            )

        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nombre de usuario'}),
            #'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Email'}),
            }

class ProfesionalForm(forms.ModelForm):
     class Meta():
        model = Profesional
        fields = (
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            #'es_alumno',
            'run',
            'fecha_Nacimiento',
            'domicilio',
            'ciudad',
            'telefono',
            )

        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese nombre del Profesional'}),
            'apellido_paterno' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese apellido paterno del Profesional'}),
            'apellido_materno' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese apellido materno del Profesional'}),
            #'es_alumno' : forms.CheckboxInput(attrs={}),
            'run' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : '11.111.111-1'}),
            'fecha_nacimiento' : forms.DateInput(attrs={'class': 'form-control  pull-right', 'id' : 'datepicker'}),
            'domicilio' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese el domicilio del Profesional'}),
            'ciudad' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese la ciudad de recidencia del Profesional'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : '12345678'}),
        }
        