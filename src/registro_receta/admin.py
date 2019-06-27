from django.contrib import admin

# Register your models here.
from .models import Receta, AlimentoEnReceta

admin.site.register(Receta)
admin.site.register(AlimentoEnReceta)
