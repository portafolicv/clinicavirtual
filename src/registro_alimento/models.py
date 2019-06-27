from django.db import models
from profesional.models import Profesional

class Unidad_Medida(models.Model):
    
    unidad_medida = models.CharField(max_length=20)
    def __str__(self):
        return self.unidad_medida


class Envase(models.Model):
    
    envase = models.CharField(max_length=20)
    def __str__(self):
        return self.envase


class Alimento(models.Model):
    nombre = models.CharField(max_length=10)
    perecible = models.BooleanField(default=True)
    precio = models.FloatField(null=True, blank=True, default=None)
    unidad_medida = models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE, null=False)
    envase = models.ForeignKey(Envase, on_delete=models.CASCADE, null=False)
    peso_envase = models.FloatField(null=True, blank=True, default=None)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nombre




class Proteina(models.Model):
    nombre = models.CharField(max_length=20)
    unidad_medida = models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.nombre

class Lipido(models.Model):
    nombre = models.CharField(max_length=20)
    unidad_medida = models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.nombre

class HidratoC(models.Model):
    nombre = models.CharField(max_length=20)
    unidad_medida = models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.nombre

class Vitamina(models.Model):
    nombre = models.CharField(max_length=20)
    unidad_medida = models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.nombre

class Mineral(models.Model):
    nombre = models.CharField(max_length=20)
    unidad_medida = models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.nombre




class ProteinaAlimento(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, null=True)
    proteina = models.ForeignKey(Proteina, on_delete=models.CASCADE, null=True)
    cantidad = models.FloatField(null=True, blank=True, default=None)
    def __str__(self):
        return self.alimento.nombre + "+" + self.proteina.nombre
class LipidoAlimento(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, null=True)
    lipido = models.ForeignKey(Lipido, on_delete=models.CASCADE, null=True)
    cantidad = models.FloatField(null=True, blank=True, default=None) 
    def __str__(self):
        return self.alimento.nombre + "+" + self.lipido.nombre

class HidratoCAlimento(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, null=True)
    hidratoC = models.ForeignKey(HidratoC, on_delete=models.CASCADE, null=True)
    cantidad = models.FloatField(null=True, blank=True, default=None) 
    def __str__(self):
        return self.alimento.nombre + "+" + self.hidratoC.nombre

class VitaminaAlimento(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, null=True)
    vitamina = models.ForeignKey(Vitamina, on_delete=models.CASCADE, null=True)
    cantidad = models.FloatField(null=True, blank=True, default=None) 
    def __str__(self):
        return self.alimento.nombre + "+" + self.vitamina.nombre

class MineralAlimento(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, null=True)
    mineral = models.ForeignKey(Mineral, on_delete=models.CASCADE, null=True)
    cantidad = models.FloatField(null=True, blank=True, default=None) 
    def __str__(self):
        return self.alimento.nombre + "+" + self.mineral.nombre

