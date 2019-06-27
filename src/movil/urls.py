from django.urls import path
from movil.views import avance_view, mi_dieta_view
from welcome.views import welcome_view

urlpatterns = [
    path('home/', welcome_view, name="welcome"),
    path('mi_avance/', avance_view, name="mi_avance"),
    path('mi_dieta/', mi_dieta_view, name="mi_dieta"),
]