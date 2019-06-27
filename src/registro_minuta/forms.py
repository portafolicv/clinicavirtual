from django import forms
from .models import Minuta, RecetaEnMinuta

class MinutaForm(forms.ModelForm):
    class Meta:
        model = Minuta
        fields = [
            'nombre',
            'descripcion'        
        ]
        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese nombre de la minuta',
            }),
            'descripcion' : forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder' : 'Ingrese una corta descripción de la minuta',
            }),
        }

class RecetaEnMinutaForm(forms.ModelForm):
    class Meta:
        model = RecetaEnMinuta
        fields = [
            'receta'
        ]
        widgets = {
            'receta' : forms.Select(
                attrs={
                'class': 'form-control',
            }),
        }