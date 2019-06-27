from django.db import models
from django.contrib.auth.models import User, Permission
from datetime import datetime



class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    es_alumno = models.BooleanField(default=True)
    run = models.CharField(max_length=12)
    fecha_Nacimiento = models.DateField(default= datetime.today, blank=True)
    domicilio = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + " " + self.apellido_paterno




#metodo publico para comprobar los permisos de usuario
#funca!!!
def EvaluarPermisos(id):

    #construye el usuario a evaluar
    usuario_a_evaluar = User.objects.get(id=id)
    #carga la lista de permisos de ese usuario
    permisos = usuario_a_evaluar.user_permissions.all()

    #crea como objeto los permisos que se buscan
    admin = Permission.objects.get(codename = 'admin_permission')
    profesional = Permission.objects.get(codename = 'profesional_permission')
    alumno = Permission.objects.get(codename = 'alumno_permission')
    paciente = Permission.objects.get(codename = 'paciente_permission')

    #evalua la lista de permisos del usuario y retorna una cadena
    for permiso in permisos:

        if permiso == admin:
            return "es_admin"

        elif permiso == profesional:
            return "es_profesional"
        
        elif permiso == alumno:
            return "es_alumno"
        
        elif permiso == paciente:
            return "es_paciente"

    #si el usuario no tiene ninguno de los permisos se retorna otra cadena
    return "sin_permisos"  