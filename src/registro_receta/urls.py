from django.urls import path
from registro_receta.views import buscar_receta_view, registro_receta_view, editar_receta_view, remover_receta_view, remover_alimentoenreceta_view

urlpatterns = [
    path('buscar_receta/', buscar_receta_view, name="buscar_receta"),
    path('registro_receta/', registro_receta_view, name="ingreso_receta"),
    path('<int:id_rc>/editar_receta/', editar_receta_view, name="editar_receta"),
    path('<int:id_rc>/remover_receta/', remover_receta_view, name="remover_receta"),
    path('<int:id_rc>/<int:id_alimentoenreceta>/remover_alimentoenreceta/', remover_alimentoenreceta_view, name="remover_alimentoenreceta")
]

