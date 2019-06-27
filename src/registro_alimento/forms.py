from django import forms
from .models import Alimento
from .models import Vitamina, Mineral, HidratoC, Lipido, Proteina
from .models import VitaminaAlimento, MineralAlimento, HidratoCAlimento, LipidoAlimento, ProteinaAlimento



#region AlimentoForm
class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = [
            'nombre',
            'perecible',
            'precio',
            'unidad_medida',
            'envase',
            'peso_envase',
        ]
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese nombre del alimento'
            }),
            'perecible' : forms.CheckboxInput(attrs={

            }),
            'precio' : forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder' : '1111'
            }),
            'unidad_medida' : forms.Select(attrs={
                'class': 'form-control', 
            }),
            'envase' :forms.Select(attrs={
                'class': 'form-control', 
            }),
            'peso_envase' : forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Indique el peso del envase'
            }),
        }
#endregion

#region VitaminaForm
class VitaminaForm(forms.ModelForm):
    class Meta:
        model = Vitamina
        fields = [
            'nombre', 
            'unidad_medida',            
            ]
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese nombre de vitamina'
            }),
            'unidad_medida' : forms.Select(attrs={
                'class': 'form-control', 
            }),
        }
#endregion

#region VitaminaAlimentoForm
class VitaminaAlimentoForm(forms.ModelForm):
    class Meta:
        model = VitaminaAlimento
        fields = [
            'vitamina',
            'cantidad',
        ]
        widgets = {
            'vitamina' : forms.Select(attrs={
                'class': 'form-control'            
            }),
            'cantidad' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese la cantidad'
            }),
        }
#endregion

#region MineralForm
class MineralForm(forms.ModelForm):
    class Meta:
        model = Mineral
        fields = [
            'nombre', 
            'unidad_medida',
        ]
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese nombre de Mineral'
            }),
            'unidad_medida' : forms.Select(attrs={
                'class': 'form-control', 
            }),
        }
#endregion

#region MineralAlimentoForm
class MineralAlimentoForm(forms.ModelForm):
    class Meta:
        model = MineralAlimento
        fields = [
            'mineral',
            'cantidad',
        ]
        widgets = {
            'mineral' : forms.Select(attrs={
                'class': 'form-control'            
            }),
            'cantidad' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese la cantidad'
            }),
        }
#endregion

#region HidratoCForm
class HidratoCForm(forms.ModelForm):
    class Meta:
        model = HidratoC
        fields = [
            'nombre',
            'unidad_medida',
        ]
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese nombre de Mineral'
            }),
            'unidad_medida' : forms.Select(attrs={
                'class': 'form-control', 
            }),
        }
#endregion

#region HidratoCAlimentoForm
class HidratoCAlimentoForm(forms.ModelForm):
    class Meta:
        model = HidratoCAlimento
        fields = [
            'cantidad',
        ]
        widgets = {
            'cantidad' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese la cantidad'
            }),
        }
#endregion

#region LipidoForm
class LipidoForm(forms.ModelForm):
    class Meta:
        model = Lipido
        fields = [
            'nombre',
            'unidad_medida',
        ]
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese nombre de Mineral'
            }),
            'unidad_medida' : forms.Select(attrs={
                'class': 'form-control', 
            }),
        }
#endregion

#region LipidoAlimentoForm

class LipidoAlimentoForm(forms.ModelForm):
    class Meta:
        model = LipidoAlimento
        fields = [
            'lipido',
            'cantidad',
        ]
        widgets = {
            'lipido' : forms.Select(attrs={
                'class': 'form-control'  
            }),
            'cantidad' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese la cantidad'
            }),
        }
#endregion

#region ProteinaForm
class ProteinaForm(forms.ModelForm):
    class Meta:
        model = Proteina
        fields = [
            'nombre',
            'unidad_medida',
        ]
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese nombre de Mineral'
            }),
           'unidad_medida' : forms.Select(attrs={
                'class': 'form-control', 
            }),
        }
#endregion

#region ProteinaAlimentoForm
class ProteinaAlimentoForm(forms.ModelForm):
    class Meta:
        model = ProteinaAlimento
        fields = [
            'cantidad',
        ]
        widgets = {
            'cantidad' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder' : 'Ingrese la cantidad'
            }),
        }
#endregion