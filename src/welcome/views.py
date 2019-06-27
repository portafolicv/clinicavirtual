from django.http import HttpResponse
from profesional.models import Profesional
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.shortcuts import render

def welcome_view(request):

    #verificacion de la existencia de los permisos necesarios
    ct = ContentType.objects.get_for_model(Profesional)
    Permission.objects.get_or_create(name='admin_permission', codename='admin_permission', content_type=ct)
    Permission.objects.get_or_create(name='profesional_permission', codename='profesional_permission', content_type=ct)
    Permission.objects.get_or_create(name='alumno_permission', codename='alumno_permission', content_type=ct)
    Permission.objects.get_or_create(name='paciente_permission', codename='paciente_permission', content_type=ct)
    
    return render(request, "index.html", {})

def main_view(request, *args, **kwargs):
    return render(request, "home.html", {})