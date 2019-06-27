from django.contrib import admin
from .models import Escolaridad, Estado_Civil, Paciente, Prevision

# Register your models here.
admin.site.register(Escolaridad)
admin.site.register(Prevision)
admin.site.register(Estado_Civil)
admin.site.register(Paciente)