from django.contrib import admin
from .models import Anamnesis, AntAlimenticios, AntFamiliar, AntHabitos, AntInicial, AntSalud

# Register your models here.
admin.site.register(Anamnesis)
admin.site.register(AntAlimenticios)
admin.site.register(AntFamiliar)
admin.site.register(AntHabitos)
admin.site.register(AntInicial)
admin.site.register(AntSalud)