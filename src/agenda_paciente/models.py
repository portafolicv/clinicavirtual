from django.db import models
from gestion_paciente.models import Paciente
from profesional.models import Profesional
from registro_minuta.models import Minuta

# Create your models here.

# Modelo control medico
class ControlMedico(models.Model):
    fechaControl = models.DateField(blank=True)
    horaControl = models.DateTimeField(null=True)
    asiste = models.BooleanField(default=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=False)



class Minuta_Paciente(models.Model):
    minuta = models.ForeignKey(Minuta, on_delete=models.CASCADE, null=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False)
    observaciones = models.CharField(max_length=200)