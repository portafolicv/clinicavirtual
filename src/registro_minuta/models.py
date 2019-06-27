from django.db import models
from profesional.models import Profesional
from registro_receta.models import Receta

# Create your models here.
class Minuta(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=100, null=True)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=False)

class RecetaEnMinuta(models.Model):
    minuta = models.ForeignKey(Minuta, on_delete=models.CASCADE, null=False)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, null=False)