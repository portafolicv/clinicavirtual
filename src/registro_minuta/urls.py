from django.urls import path
from registro_minuta.views import buscar_minuta_view, registro_minuta_view, editar_minuta_view, remover_minuta_view, remover_recetaenminuta_view

urlpatterns = [
    path('buscar_minuta/', buscar_minuta_view, name="buscar_minuta"),
    path('registro_minuta/', registro_minuta_view, name="ingreso_minuta"),
    path('<int:id_minuta>/editar_minuta/', editar_minuta_view, name="editar_minuta"),
    path('<int:id_minuta>/remover_minuta/', remover_minuta_view, name="remover_minuta"),
    path('<int:id_minuta>/<int:id_recetaenminuta>/remover_recetaenminuta/', remover_recetaenminuta_view, name="remover_recetaenminuta")
]