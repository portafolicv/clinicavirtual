from django.db import models
from profesional.models import Profesional
from registro_alimento.models import Alimento

class TipoServicioReceta(models.Model):
    tipo =models.CharField(max_length=12, unique=True, null=False)
    def __str__(self):
        return self.tipo

class Receta(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    preparacion = models.TextField(null=True)
    tipoServicio = models.ForeignKey(TipoServicioReceta, on_delete=models.CASCADE, null=False)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.nombre

class AlimentoEnReceta(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, null=False)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, null=False)
    pesoBruto = models.FloatField(null=True, blank=True, default=None) 
    pesoNeto = models.FloatField(null=True, blank=True, default=None) 