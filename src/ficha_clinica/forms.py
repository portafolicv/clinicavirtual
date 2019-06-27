from django import forms
from .models import *


#Formularios Anamnesis===================================
class AnamnesisForm(forms.ModelForm):
    class Meta:
        model = Anamnesis
        fields = '__all__'
        
        widgets = {
            'paciente' : forms.Select(attrs={'class' : 'form-control'}),
        }

class AntInicialForm(forms.ModelForm):
    class Meta:
        model = AntInicial
        fields = '__all__'
        exclude = ['anamnesis']
        
        widgets = {
            'edad' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese edad de paciente'}), 
            'estatura': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese estatura de paciente'}), 
            'imc': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese IMC de paciente'}), 
            'estado_nutricional': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Indique estado nutricional de paciente', 'type': 'text'}), 
            'peso': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese peso de paciente'}),
            'sexo': forms.RadioSelect(choices=AntInicial.sexo_choise),
            'ocupacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Indique ocupación de paciente'}),
            'motivo_consulta': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Indique motivo de la consulta'}),
        }        

class AntSaludForm(forms.ModelForm):
    class Meta:
        model = AntSalud
        fields = '__all__'
        exclude = ['anamnesis']

        widgets = {
            'enferm_diagnosticada' : forms.RadioSelect(choices=AntSalud.enferm_choise),
            'desc_enfermedad' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese enfermedades indicadas por el paciente'}),
            'medicacion' : forms.RadioSelect(choices=AntSalud.med_choise),
            'desc_medicacion' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Indique medicamentos consumidos por paciente'}),
        }

class AntHabitosForm(forms.ModelForm):
    class Meta:
        model = AntHabitos
        fields = '__all__'
        exclude = ['anamnesis']

        widgets = {
            'fuma' : forms.RadioSelect(choices=AntHabitos.fuma_choise),
            'bebe' : forms.RadioSelect(choices=AntHabitos.bebe_choise),
            'usa_drogas' : forms.RadioSelect(choices=AntHabitos.drogas_choise),
            'descrip_droga' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Indique drogas consumidas por el paciente'}),
        }        

class AntFamiliarForm(forms.ModelForm):
    class Meta:
        model = AntFamiliar
        fields = '__all__'
        exclude = ['anamnesis']

        widgets = {
            'cant_integrantes' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Cantidad de integrantes de nucleo familiar'}),
            'situacion_econom' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Indique situación economica de paciente'}),
            'morbilidades' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Indique información familiar, padres y/o abuelos. Datos como Dm, Hta, Dlp u otros.'}),
        }

class AntAlimenticiosForm(forms.ModelForm):
    class Meta:
        model = AntAlimenticios
        fields = '__all__'
        exclude = ['anamnesis']
        
        widgets = {
            'liquidos' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese tipos de liquido que ingiere el paciente'}),
            'cantidad_liquido' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese cantidad de liquido que ingiere el paciente'}),
            'habitos_comida' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese habitos y/o costumbres al comer (come acostado, de pie, etc)'}),
            'encargado_cocina' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Indique quien cocina en el hogar'}),
            'actividad_fisica' : forms.RadioSelect(choices=AntAlimenticios.act_fisica_choise),
            'desc_act_fisica' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : '¿Que actividad fisica?'}),
            'tiempo_act_fisica' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Indique cantidad de tiempo que le dedica'}),
            'objetivo_intervencion' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Indique los objetivos de la intervención'}),
        }


#Formularios ficha clinica===========================================================
class FichaClinicaForm(forms.ModelForm):
    class Meta:
        model = FichaClinica
        fields = '__all__'
        exclude = ['fecha']

        widgets = {
            'paciente' : forms.Select(attrs={'class' : 'form-control'}),
        }

class DatosActualesForm(forms.ModelForm):
    class Meta:
        model = DatosActuales
        fields = '__all__'
        exclude =  ['ficha']

        widgets = {
            'imc' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese IMC de su paciente'}),
            'estado_nutricional' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese estado nutricional de su paciente'}),
            'peso_actual' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese peso actual de su paciente'}),
            'comentarios' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Indique algun comentario'}),
            'objetivos' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Indique los objetivos de la intervención'}),
            'diagnostico' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Indique el diagnostico nutricional del paciente'}),
            'observaciones' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Indique alguna observación sobre el paciente'}),
        }

#habitos actuales

class HabitosActualesForm(forms.ModelForm):
    class Meta:
        model = HabitosActuales
        fields = '__all__'

        exclude = ['ficha']

        widgets = {
            'habito' : forms.Select(attrs={'class' : 'form-control'}),
        }

class IndBioquimicoActualForm(forms.ModelForm):
    class Meta:
        model = IndBioquimicoActual
        fields = '__all__'

        exclude = ['ficha']

        widgets = {
            'indice' : forms.Select(attrs={'class' : 'form-control'}),
            'niveles' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Indique niveles presentes'}),
        }

class IndClinicoActualForm(forms.ModelForm):
    class Meta:
        model = IndClinicoActual
        fields = '__all__'

        exclude = ['ficha']

        widgets = {
            'indice' : forms.Select(attrs={'class' : 'form-control'}),
            'niveles' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Indique niveles presentes'}),
        }

class AntPatologicoFamiliarForm(forms.ModelForm):
    class Meta:
        model = PatologiaFamiliar
        fields = '__all__'
        exclude = ['ficha']

        widgets = {
            'patologia' : forms.Select(attrs={'class' : 'form-control'}),
        }        

class AntPatologicoPacienteForm(forms.ModelForm):
    class Meta:
        model = PatologiaPaciente
        fields = '__all__'
        exclude = ['ficha']

        widgets = {
            'patologia' : forms.Select(attrs={'class' : 'form-control'}),
        }

class ProblemasActualesForm(forms.ModelForm):
    class Meta:
        model = SintomaActual
        fields = '__all__'
        exclude = ['ficha']

        widgets = {
            'sintoma' : forms.Select(attrs={'class' : 'form-control'}),
        }

#imputs mantenedores modales====================================================================
class HabitoForm(forms.ModelForm):
    class Meta:
        model = TipoHabito
        fields = [
            'descripcion',            
            ]
        widgets = {
            'descripcion' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese nuevo habito a su lista'}),
        }

class SintomaForm(forms.ModelForm):
    class Meta:
        model = TipoSintoma
        fields = [
            'descripcion',            
            ]
        widgets = {
            'descripcion' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese nuevo sintoma a su lista'}),
        }

class IndBioquimicoForm(forms.ModelForm):
    class Meta:
        model = IndiceBioquimico
        fields = [
            'descripcion',            
            ]
        widgets = {
            'descripcion' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese nuevo indicador bioquímico a su lista'}),
        }

class IndClinicoForm(forms.ModelForm):
    class Meta:
        model = IndiceClinico
        fields = [
            'descripcion',            
            ]
        widgets = {
            'descripcion' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese nuevo indicador clinico a su lista'}),
        }        

class PatologiaForm(forms.ModelForm):
    class Meta:
        model = TipoPatologia
        fields = [
            'descripcion',            
            ]
        widgets = {
            'descripcion' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese nueva patología a su lista'}),
        }