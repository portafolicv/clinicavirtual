from django.contrib import admin

# Register your models here.
from .models import Minuta, RecetaEnMinuta

admin.site.register(Minuta)
admin.site.register(RecetaEnMinuta)

