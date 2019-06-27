from django.shortcuts import render, redirect
from django.urls import reverse
from gestion_paciente.models import Paciente
from ficha_clinica.models import *
from gpcharts import figure
#import numpy as np

"""
pip install gpcharts
pip install numpy
"""

# Create your views here.
def avance_view(request):
    usr = request.user
    idPac = Paciente.objects.get(user_id=usr.id).id
    
    idAnamnesis = Anamnesis.objects.get(paciente_id=idPac)
    id_ecivil = Paciente.objects.get(id=idPac).estado_id

    estatura = AntInicial.objects.get(anamnesis=idAnamnesis).estatura
    imc = AntInicial.objects.get(anamnesis=idAnamnesis).imc
    estado_nutricional = AntInicial.objects.get(anamnesis=idAnamnesis).estado_nutricional
    peso = AntInicial.objects.get(anamnesis=idAnamnesis).peso

    fichas_id = FichaClinica.objects.filter(paciente_id=idPac).values_list('pk', flat=True)
    
    imc_fichas = []
    peso_fichas = []
    for ficha in fichas_id:
        imc_fichas.append(int(float(DatosActuales.objects.get(ficha_id=ficha).imc)))
        peso_fichas.append(int(float(DatosActuales.objects.get(ficha_id=ficha).peso_actual)))

    #grafico IMC
    imc_chart = int(float(imc))
    
    #grafico Peso
    peso_chart = int(float(peso))
   
    context = {
        "estatura" : estatura,
        "imc" : imc,
        "estado_nutricional" : estado_nutricional,
        "peso" : peso,
        "imc_chart" : imc_chart,
        "peso_chart" : peso_chart,
        "imc_fichas" : imc_fichas,
        "peso_fichas" : peso_fichas,
        
    }
    return render(request, "paciente_views/avance.html", context)

def mi_dieta_view(request):
    
    return render(request, "paciente_views/dietas.html", {})