from django.urls import path
from ficha_clinica.views import *

urlpatterns = [
    path('anamnesis/', anamnesis_paciente_view, name="anamnesis_paciente"),
    path('crear_anamnesis/anamnesis_<id_anamnesis>/',crear_anamnesis_view, name="crear_anamnesis"),
    path('buscar_ficha/', buscar_ficha_view, name="buscar_ficha"),
    path('nueva_ficha/', nueva_ficha_view, name="nueva_ficha"),
    path('crear_ficha/ficha_<id_ficha>_habitos_indicadores/', crear_ficha_view, name="crear_ficha"),
    path('crear_ficha/ficha_<ficha_id>_antecedentes_analisis/', analisis_ficha_view, name="analisis_ficha"),
    path('crear_ficha/succes/', succes_view, name="succes"),
]