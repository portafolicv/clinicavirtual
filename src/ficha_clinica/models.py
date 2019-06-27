from django.db import models
from gestion_paciente.models import Paciente
from datetime import datetime
# Create your models here.

# Anamnesis
class Anamnesis(models.Model):
    fecha = models.DateField(default= datetime.today, blank=True)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    
# Informes anamnesis
class AntInicial(models.Model):
    #definir las opciones de los radio button y choice
    Masculino = 'Masculino'
    Femenino = 'Femenino'
    sexo_choise=((Masculino,'Masculino'),(Femenino,'Femenino'))
    edad = models.PositiveIntegerField(null=False)
    estatura = models.FloatField(null=True, blank=True, default=None)
    imc = models.FloatField(null=True, blank=True, default=None)
    estado_nutricional = models.CharField(max_length=30)
    peso = models.FloatField(null=True, blank=True, default=None)
    sexo = models.CharField(choices=sexo_choise, default=Masculino, max_length=9)
    ocupacion = models.CharField(max_length=30)
    motivo_consulta = models.TextField(blank=True)
    anamnesis = models.OneToOneField(Anamnesis, on_delete=models.CASCADE)

class AntHabitos(models.Model):
    No = 'No'
    Si = 'Si'
    fuma_choise = ((No, 'No'),(Si, 'Si'))
    bebe_choise = ((No, 'No'),(Si, 'Si'))
    drogas_choise = ((No, 'No'),(Si, 'Si'))

    fuma = models.CharField(choices=fuma_choise, default=No, max_length=2)
    bebe = models.CharField(choices=bebe_choise, default=No, max_length=2)
    usa_drogas = models.CharField(choices=drogas_choise, default=No, max_length=2)
    descrip_droga = models.CharField(max_length=30,null=True, blank=True)
    anamnesis = models.OneToOneField(Anamnesis, on_delete=models.CASCADE)

class AntSalud(models.Model):
    No = 'No'
    Si = 'Si'
    enferm_choise = ((No, 'No'),(Si, 'Si'))
    med_choise = ((No, 'No'),(Si, 'Si'))

    enferm_diagnosticada = models.CharField(choices=enferm_choise, default=No, max_length=2)
    desc_enfermedad = models.CharField(max_length=30,null=True, blank=True)
    medicacion = models.CharField(choices=med_choise, default=No, max_length=2)
    desc_medicacion = models.CharField(max_length=30,null=True, blank=True)
    anamnesis = models.OneToOneField(Anamnesis, on_delete=models.CASCADE)

class AntFamiliar(models.Model):
    cant_integrantes = models.PositiveSmallIntegerField()
    situacion_econom = models.CharField(max_length=30)
    morbilidades = models.TextField(blank=True)
    anamnesis = models.OneToOneField(Anamnesis, on_delete=models.CASCADE)

class AntAlimenticios(models.Model):
    NINGUNA = 'NINGUNA'
    SEDENTARIO = 'SEDENTARIO'
    LIVIANA = 'LIVIANA'
    MODERADA = 'MODERADA'
    INTENSA = 'INTENSA'
    act_fisica_choise = ((NINGUNA, 'Ninguna'),(SEDENTARIO, 'Sedentario'),(LIVIANA, 'Liviana'),(MODERADA, 'Moderada'), (INTENSA, 'Intensa'))

    liquidos = models.CharField(max_length=50)
    cantidad_liquido = models.FloatField(null=True, blank=True, default=None)
    habitos_comida = models.CharField(max_length=100)
    encargado_cocina =  models.CharField(max_length=50)
    actividad_fisica = models.CharField(choices=act_fisica_choise, default=NINGUNA, max_length=12)
    desc_act_fisica = models.CharField(max_length=20)
    tiempo_act_fisica = models.CharField(max_length=50)
    objetivo_intervencion = models.TextField(blank=True)
    anamnesis = models.OneToOneField(Anamnesis, on_delete=models.CASCADE)

# Ficha clinica ======================================================================= 

class FichaClinica(models.Model):
    fecha = models.DateField(default= datetime.today)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class DatosActuales(models.Model):
    imc = models.FloatField(default=None)
    estado_nutricional = models.CharField(max_length=20)
    peso_actual = models.FloatField(default=None)
    comentarios = models.TextField(blank=True)
    objetivos = models.TextField(blank=True)
    diagnostico = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    ficha = models.ForeignKey(FichaClinica, null=True, blank=True, on_delete=models.CASCADE)   

# Ficha clinica - habitos

class TipoHabito(models.Model):
    descripcion = models.CharField(max_length=30)
    ficha = models.ManyToManyField(FichaClinica, through='HabitosActuales')
    def __str__(self):
        return self.descripcion   

class HabitosActuales(models.Model):
    habito = models.ForeignKey(TipoHabito, on_delete=models.CASCADE)
    ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)      

# Ficha clinica - tipo sintomas =======================
class TipoSintoma(models.Model):
    descripcion = models.CharField(max_length=20)
    ficha = models.ManyToManyField(FichaClinica, through='SintomaActual')
    def __str__(self):
        return self.descripcion 

class SintomaActual(models.Model):
    ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)    
    sintoma = models.ForeignKey(TipoSintoma, on_delete=models.CASCADE)

# Ficha clinica - indices bioquimicos

class IndiceBioquimico(models.Model):
    descripcion = models.CharField(max_length=20)
    ficha = models.ManyToManyField(FichaClinica, through='IndBioquimicoActual')
    def __str__(self):
        return self.descripcion  

class IndBioquimicoActual(models.Model):
    niveles = models.FloatField(null=True, blank=True, default=None)
    indice = models.ForeignKey(IndiceBioquimico, on_delete=models.CASCADE)
    ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)

# Ficha clinica - Indice Clinico

class IndiceClinico(models.Model):
    descripcion = models.CharField(max_length=20)
    ficha = models.ManyToManyField(FichaClinica, through='IndClinicoActual')
    def __str__(self):
        return self.descripcion 

class IndClinicoActual(models.Model):
    niveles = models.FloatField(null=True, blank=True, default=None)
    indice = models.ForeignKey(IndiceClinico, on_delete=models.CASCADE)    
    ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)

# Ficha Clinica - Patologias

class TipoPatologia(models.Model):
    descripcion = models.CharField(max_length=20)
    def __str__(self):
        return self.descripcion 
# Patologias familiares

class PatologiaFamiliar(models.Model):
    ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)    
    patologia = models.ForeignKey(TipoPatologia, on_delete=models.CASCADE)

# Patoligias de paciente 

class PatologiaPaciente(models.Model):
    ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)    
    patologia = models.ForeignKey(TipoPatologia, on_delete=models.CASCADE)   

