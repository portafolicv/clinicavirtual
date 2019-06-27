"""Clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import include, path

from welcome.views import welcome_view, main_view
from agenda_paciente.views import agendar_visita_view, ver_agenda_view
from gestion_paciente.views import buscar_paciente_view, registro_paciente_view
from registro_alimento.views import buscar_alimento_view, registro_alimento_view
from registro_receta.views import buscar_receta_view, registro_receta_view
from registro_minuta.views import buscar_minuta_view, registro_minuta_view
from movil.views import avance_view, mi_dieta_view


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', welcome_view, name="welcome"),
    path('home/', main_view, name="home"),
    path('agenda/', include('agenda_paciente.urls')),
    path('paciente/', include('gestion_paciente.urls')),
    path('ficha_clinica/', include('ficha_clinica.urls')),
    path('alimento/', include('registro_alimento.urls')),
    path('receta/', include('registro_receta.urls')),
    path('minuta/', include('registro_minuta.urls')),
    path('profesional/', include('profesional.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('myapp/', include('movil.urls')),
        
]
