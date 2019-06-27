from django.urls import path
from registro_alimento.views import buscar_alimento_view, registro_alimento_view, editar_alimento_view, rm_alimento_view, rm_componente_view

urlpatterns = [
    path('buscar_alimento/', buscar_alimento_view, name="buscar_alimento"),
    path('registro_alimento/', registro_alimento_view, name="ingreso_alimento"),
    path('<int:id_al>/editar_alimento/', editar_alimento_view, name= "editar_alimento"),
    path('<int:id_al>/rm_alimento/', rm_alimento_view, name="remover_alimento"),
    path('<int:id_al>/<int:tipo>/<int:id_comp>/rm_componente/', rm_componente_view, name="remover_componente"),
]