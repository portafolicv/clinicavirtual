from django.urls import path
from gestion_paciente.views import buscar_paciente_view, registro_paciente_view, registro_datos_paciente_view
from ficha_clinica.views import succes_view

urlpatterns = [
    path('buscar_paciente/', buscar_paciente_view, name="buscar_paciente"),
    path('registro_paciente/', registro_paciente_view, name="registrar_paciente"),
    path('<int:paciente_id>/registro_datos_paciente/', registro_datos_paciente_view, name="registrar_datos_paciente"),
    path('crear_ficha/succes/', succes_view, name="succes"),
]
