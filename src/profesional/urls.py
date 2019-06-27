from django.urls import path
from .views import user_login, user_logout, user_charge, registrar_profesional_view, registrar_datos_profesional_view

urlpatterns = [
    path('', user_login, name="user_login"),
    path('logout/', user_logout, name="logout"),
    path('user_charge/', user_charge, name="charge"),
    path('registrar_profesional/', registrar_profesional_view, name="registrar_profesional"),
    path('<int:profesional_id>/registrar_datos_profesional/', registrar_datos_profesional_view, name="registrar_datos_profesional"),
]