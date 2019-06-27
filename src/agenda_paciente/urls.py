from django.urls import path
from agenda_paciente.views import agendar_visita_view, ver_agenda_view, modificar_visita_view

urlpatterns = [
    path('ver_agenda/', ver_agenda_view, name="ver_agenda"),
    path('agendar_visita/', agendar_visita_view, name="agendar_visita"),
    path('modificar_hora/', modificar_visita_view, name="modificar_visita"),
]