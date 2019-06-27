from django import forms
from .models import Receta, AlimentoEnReceta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'nombre',
            'tipoServicio'        
        ]
        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese nombre de la receta',
                'required': False,
            }),
            'tipoServicio' : forms.Select(
                attrs={
                'class': 'form-control',
                'required': False,
            }),
        }

class AlimentoEnRecetaForm(forms.ModelForm):
    class Meta:
        model = AlimentoEnReceta
        fields = [
            'alimento',
            'pesoBruto',
            'pesoNeto'
        ]
        widgets = {
            'alimento' : forms.Select(attrs={
                'class': 'form-control'
            }),
            'pesoBruto' : forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder' : '1111'
            }),
            'pesoNeto' : forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder' : '1111'
            }),
        }