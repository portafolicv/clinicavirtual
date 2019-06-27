from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import *

# Create your views here.
def anamnesis_paciente_view(request):
    form_anamnesis = AnamnesisForm(request.POST)
    if form_anamnesis.is_valid():
        form_anamnesis.save()
        id_anamnesis = Anamnesis.objects.latest('id').id
        return redirect('crear_anamnesis', id_anamnesis = id_anamnesis)
    
    context = {
        "form_anamnesis" : form_anamnesis,
    }    
    return render(request, "anamnesis.html", context)

def crear_anamnesis_view(request, id_anamnesis):
    anamnesis_id = Anamnesis.objects.get(id=id_anamnesis)
    print("id obtenida", anamnesis_id)
    paciente_anamnesis = Paciente.objects.get(id=anamnesis_id.paciente.id)
    print(paciente_anamnesis)
    
    if request.method == 'POST':
        form_AntInicial = AntInicialForm(request.POST, prefix='antInicial')
        form_AntSalud = AntSaludForm(request.POST, prefix='antSalud')
        form_AntHabito =  AntHabitosForm(request.POST, prefix='antHabito')
        form_AntFamiliar = AntFamiliarForm(request.POST, prefix='antFamiliar')
        form_AntAlimenticios = AntAlimenticiosForm(request.POST, prefix='antAlimenticios')

        AntInicial = form_AntInicial.is_valid()
        AntSalud = form_AntSalud.is_valid()
        AntHabito =  form_AntHabito.is_valid()
        AntFamiliar = form_AntFamiliar.is_valid()
        AntAlimenticios = form_AntAlimenticios.is_valid()

        print(AntInicial, AntSalud, AntHabito, AntFamiliar, AntAlimenticios)

        if AntInicial and AntSalud and AntHabito and AntFamiliar and AntAlimenticios:
            ant_inicial = form_AntInicial.save(commit=False)
            ant_salud = form_AntSalud.save(commit=False)
            ant_habito = form_AntHabito.save(commit=False)
            ant_familiar = form_AntFamiliar.save(commit=False)
            ant_alimento = form_AntAlimenticios.save(commit=False)
            
            ant_inicial.anamnesis = anamnesis_id
            ant_inicial.save()
            ant_salud.anamnesis = anamnesis_id
            ant_salud.save()
            ant_habito.anamnesis = anamnesis_id
            ant_habito.save()
            ant_familiar.anamnesis = anamnesis_id
            ant_familiar.save()
            ant_alimento.anamnesis = anamnesis_id
            ant_alimento.save()
            return redirect('succes')
             
    context = {
        "form_AntInicial" : AntInicialForm(prefix='antInicial'),
        "form_AntSalud" : AntSaludForm(prefix='antSalud'),
        "form_AntHabito" : AntHabitosForm(prefix='antHabito'),
        "form_AntFamiliar" : AntFamiliarForm(prefix='antFamiliar'),
        "form_AntAlimenticios" : AntAlimenticiosForm(prefix='antAlimenticios'),
        'paciente_anamnesis' : paciente_anamnesis,
    }    
    return render(request, "crear_anamnesis.html", context)


def buscar_ficha_view(request):
    return render(request, "buscar_ficha.html", {})


#vista donde se selecciona paciente para crear ficha###########################################################
def nueva_ficha_view(request):
    form_ficha = FichaClinicaForm(request.POST)
    if form_ficha.is_valid():
        form_ficha.save()
        id_ficha = FichaClinica.objects.latest('id').id
        return redirect('crear_ficha', id_ficha = id_ficha)
    
    context = {
        "form_ficha" : form_ficha,
    }
    return render(request, "nueva_ficha_clinica.html", context)



####  vista creación nueva ficha=====================================
def crear_ficha_view(request, id_ficha):
    ficha_id = FichaClinica.objects.get(id=id_ficha)
    print(ficha_id)
    
    form_datos_actuales = DatosActualesForm(request.POST, prefix='ficha')
    if form_datos_actuales.is_valid():
        ficha = form_datos_actuales.save(commit=False)
        ficha.ficha = ficha_id
        ficha.save()

    if 'btn_habitos' in request.POST:
        form_habitos_actuales = HabitosActualesForm(request.POST, prefix='habitos')
        if form_habitos_actuales.is_valid():
            habitos = form_habitos_actuales.save(commit=False)
            habitos.ficha = ficha_id
            habitos.save()
            
    if 'btn_indBioquimico' in request.POST:
        form_ind_bioquimico_actual = IndBioquimicoActualForm(request.POST, prefix='ind_bioquimicos')
        if form_ind_bioquimico_actual.is_valid():
            ind_bioquimico = form_ind_bioquimico_actual.save(commit=False)
            ind_bioquimico.ficha = ficha_id
            ind_bioquimico.save()

    if 'btn_indClinico' in request.POST:
        form_ind_clinico_actual = IndClinicoActualForm(request.POST, prefix='ind_clinicos')
        if form_ind_clinico_actual.is_valid():
            ind_clinico = form_ind_clinico_actual.save(commit=False)
            ind_clinico.ficha = ficha_id
            ind_clinico.save()

    if 'btn_pat_fam' in request.POST:
        form_pat_familiar = AntPatologicoFamiliarForm(request.POST, prefix='ant_pat_familiar')
        if form_pat_familiar.is_valid():
            ant_pat_familiar = form_pat_familiar.save(commit=False)
            ant_pat_familiar.ficha = ficha_id
            ant_pat_familiar.save()

    if 'btn_pat_per' in request.POST:
        form_pat_personal = AntPatologicoPacienteForm(request.POST, prefix='ant_pat_personal')
        if form_pat_personal.is_valid():
            ant_pat_personal = form_pat_personal.save(commit=False)
            ant_pat_personal.ficha =  ficha_id
            ant_pat_personal.save()    

    if 'btn_sintomas' in request.POST:
        form_problemas_actuales = ProblemasActualesForm(request.POST, prefix='problemas_actuales')
        if form_problemas_actuales.is_valid():
            problemas_actuales = form_problemas_actuales.save(commit=False)
            problemas_actuales.ficha = ficha_id
            problemas_actuales.save()

    if request.GET.get('continuar'):
        return redirect('analisis_ficha', ficha_id=ficha_id.id)

    #mantenedores
    form_habito = HabitoForm(request.POST, prefix='habito')
    if form_habito.is_valid():
        form_habito.save()
  
    form_ind_bioquimico = IndBioquimicoForm(request.POST, prefix='ind_bio')
    if form_ind_bioquimico.is_valid():
        form_ind_bioquimico.save()
    
    form_ind_clinico = IndClinicoForm(request.POST, prefix='ind_cli')
    if form_ind_clinico.is_valid():
        form_ind_clinico.save()
    
    form_patologia = PatologiaForm(request.POST, prefix='patologia')
    if form_patologia.is_valid():
        form_patologia.save()

    form_sintoma = SintomaForm(request.POST, prefix='sintoma')
    if form_sintoma.is_valid():
        form_sintoma.save()    

    #cbox 
    habito = TipoHabito.objects.all()
    indbio = IndiceBioquimico.objects.all()
    indcli = IndiceClinico.objects.all()
    patologia = TipoPatologia.objects.all()
    sintoma = TipoSintoma.objects.all() 
                
    #views
    habitoPac = HabitosActuales.objects.all()
    indbioPac = IndBioquimicoActual.objects.all()
    indcliPac = IndClinicoActual.objects.all()
    patologiaFam = PatologiaFamiliar.objects.all()
    patologiaPac = PatologiaPaciente.objects.all()
    sintomaPac = SintomaActual.objects.all()

    #datos paciente
    idPac = FichaClinica.objects.latest('paciente').paciente_id
    idAnamnesis = Anamnesis.objects.get(paciente_id=idPac)
    id_ecivil = Paciente.objects.get(id=idPac).estado_id

    nombre = FichaClinica.objects.latest('paciente').paciente
    sexo = AntInicial.objects.get(anamnesis=idAnamnesis).sexo
    fecha_nac = Paciente.objects.get(id=idPac).fecha_nacimiento
    escolaridad = Paciente.objects.get(id=idPac).escolaridad
    e_civil = estado_civil.objects.get(id=id_ecivil).estado
    prevision = Paciente.objects.get(id=idPac).prevision
    edad = AntInicial.objects.get(anamnesis=idAnamnesis).edad
    estatura = AntInicial.objects.get(anamnesis=idAnamnesis).estatura
    imc = AntInicial.objects.get(anamnesis=idAnamnesis).imc
    estado_nutricional = AntInicial.objects.get(anamnesis=idAnamnesis).estado_nutricional
    peso = AntInicial.objects.get(anamnesis=idAnamnesis).peso
    ocupacion = AntInicial.objects.get(anamnesis=idAnamnesis).ocupacion
    motivo = AntInicial.objects.get(anamnesis=idAnamnesis).motivo_consulta

    context = {
        "form_datos_actuales" : DatosActualesForm(prefix='ficha'),
        "form_habitos_actuales" : HabitosActualesForm(prefix='habitos'),
        "form_ind_bioquimico_actual" : IndBioquimicoActualForm(prefix='ind_bioquimicos'),
        "form_ind_clinico_actual" : IndClinicoActualForm(prefix='ind_clinicos'),
        "form_pat_familiar" : AntPatologicoFamiliarForm(prefix='ant_pat_familiar'),
        "form_pat_personal" :  AntPatologicoPacienteForm(prefix='ant_pat_personal'),
        "form_problemas_actuales" : ProblemasActualesForm(prefix='problemas_actuales'),
        "form_habito": HabitoForm(prefix='habito'),
        "form_sintoma" : SintomaForm(prefix='sintoma'),
        "form_indbio" : IndBioquimicoForm(prefix='ind_bio'),
        "form_indcli" : IndClinicoForm(prefix='ind_cli'),
        "form_patologia" : PatologiaForm(prefix='patologia'),
        "form_ficha_clinica" : FichaClinicaForm(prefix='ficha_clincia'),
        "habitos" : habito,
        "indicesbio" : indbio,
        "indicescli" : indcli,
        "patologias" : patologia,
        "sintomas" : sintoma,
        "habitosPac" : habitoPac,
        "indbiosPac" : indbioPac,
        "indclinicosPac" : indcliPac,
        "patologiasFam" : patologiaFam,
        "patologiasPac" : patologiaPac,
        "sintomasPac" : sintomaPac,
        "nombre" : nombre,
        "sexo" : sexo,
        "fecha_nac" : fecha_nac,
        "escolaridad" : escolaridad,
        "est_civil" : e_civil,
        "prevision" : prevision,
        "edad" : edad,
        "estatura" : estatura,
        "imc" : imc,
        "estado_nutricional" : estado_nutricional,
        "peso" : peso,
        "ocupacion" : ocupacion,
        "motivo" : motivo,
    }
    return render(request, "crear_ficha_clinica.html", context)

def analisis_ficha_view(request, ficha_id):
    ficha = FichaClinica.objects.get(id=ficha_id)
    idPac = FichaClinica.objects.latest('paciente').paciente_id
    idAnamnesis = Anamnesis.objects.get(paciente_id=idPac)
    id_ecivil = Paciente.objects.get(id=idPac).estado_id

    nombre = FichaClinica.objects.latest('paciente').paciente
    sexo = AntInicial.objects.get(anamnesis=idAnamnesis).sexo
    fecha_nac = Paciente.objects.get(id=idPac).fecha_nacimiento
    escolaridad = Paciente.objects.get(id=idPac).escolaridad
    e_civil = estado_civil.objects.get(id=id_ecivil).estado
    prevision = Paciente.objects.get(id=idPac).prevision
    edad = AntInicial.objects.get(anamnesis=idAnamnesis).edad
    estatura = AntInicial.objects.get(anamnesis=idAnamnesis).estatura
    imc = AntInicial.objects.get(anamnesis=idAnamnesis).imc
    estado_nutricional = AntInicial.objects.get(anamnesis=idAnamnesis).estado_nutricional
    peso = AntInicial.objects.get(anamnesis=idAnamnesis).peso
    ocupacion = AntInicial.objects.get(anamnesis=idAnamnesis).ocupacion
    motivo = AntInicial.objects.get(anamnesis=idAnamnesis).motivo_consulta

    form_datos_actuales = DatosActualesForm(request.POST, prefix='datos_actuales')
    if form_datos_actuales.is_valid():
        datos_actuales = form_datos_actuales.save(commit=False)
        datos_actuales.ficha = ficha
        datos_actuales.save()
        return redirect('succes')

    context = {
        "form_datos_actuales" : DatosActualesForm(prefix='datos_actuales'),
        "nombre" : nombre,
        "sexo" : sexo,
        "fecha_nac" : fecha_nac,
        "escolaridad" : escolaridad,
        "est_civil" : e_civil,
        "prevision" : prevision,
        "edad" : edad,
        "estatura" : estatura,
        "imc" : imc,
        "estado_nutricional" : estado_nutricional,
        "peso" : peso,
        "ocupacion" : ocupacion,
        "motivo" : motivo,
    }    
    return render(request, "analisis_ficha.html", context)

def succes_view(request):
    return render(request, "succes.html", {})
