from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from profesional.models import Profesional
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

SEXO_CHOICES = ((True, 'Masculino'), (False, 'Femenino'))

class Escolaridad(models.Model):
    escolaridad = models.CharField(max_length=40)
    def __str__(self):
        return self.escolaridad

class Prevision(models.Model):
    prevision = models.CharField(max_length=40)
    def __str__(self):
        return self.prevision

# Create your models here.
class Estado_Civil(models.Model):
    estado = models.CharField(max_length=40)
    def __str__(self):
        return self.estado

# modelo del usuario paciente
class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    run = models.CharField(max_length=12)
    sexo = models.BooleanField(choices=SEXO_CHOICES, blank=False, null=False, default= True)
    fecha_nacimiento = models.DateField(default= datetime.today, blank=True)
    prevision = models.ForeignKey(Prevision, on_delete=models.CASCADE)
    escolaridad = models.ForeignKey(Escolaridad, on_delete=models.CASCADE)
    domicilio = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    ocupacion = models.CharField(max_length=30)
    profesional = models.ForeignKey(Profesional, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado_Civil, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)

    class Meta:
        permissions = (
            ('is_profesional', _('Es Profesional')),
            ('is_paciente', _('Es Paciente')),
        )
   
    
#