from django.shortcuts import render, redirect, get_object_or_404
from .forms import PacienteForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .models import Profesional, Paciente, Estado_Civil, Escolaridad, Prevision
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from profesional.models import EvaluarPermisos
from django.contrib.auth.models import Permission




@login_required
def buscar_paciente_view(request):

    usuario_activo = get_object_or_404(User, pk=request.user.id)

    permiso = EvaluarPermisos(usuario_activo.id)

    if permiso == "es_admin" or permiso == "es_profesional" or permiso == "es_alumno":
 
        if usuario_activo.is_superuser:
            paciente = Paciente.objects.all()
        else:
            prof_id = Profesional.objects.get(user = usuario_activo.id)
            paciente = Paciente.objects.filter(profesional = prof_id)
    
        context = {
            "pacientes" : paciente,
        }
        return render(request, "buscar_paciente.html", context)
    else:
        return render(request, "no_autorizado.html", {})


@login_required
def registro_paciente_view(request):

    #verificacion del poblado de la tabla estado civil, escolaridad y prevision
    Estado_Civil.objects.get_or_create(id=1, estado="Soltero/a")
    Estado_Civil.objects.get_or_create(id=2, estado="Casado/a")
    Estado_Civil.objects.get_or_create(id=3, estado="Viudo/a")
    Estado_Civil.objects.get_or_create(id=4, estado="Divorciado/a")
    Estado_Civil.objects.get_or_create(id=5, estado="Separado/a")
    Estado_Civil.objects.get_or_create(id=6, estado="Conviviente")

    Escolaridad.objects.get_or_create(id=1, escolaridad="básica incompleta")
    Escolaridad.objects.get_or_create(id=2, escolaridad="básica completa")
    Escolaridad.objects.get_or_create(id=3, escolaridad="media/tecnica incompleta")
    Escolaridad.objects.get_or_create(id=4, escolaridad="media/tecnica completa")
    Escolaridad.objects.get_or_create(id=5, escolaridad="Universitaria/I.P./C.F.T. incompleta")
    Escolaridad.objects.get_or_create(id=6, escolaridad="Universitaria/I.P./C.F.T. completa")
    Escolaridad.objects.get_or_create(id=7, escolaridad="Magister/Postgrado incompleto")
    Escolaridad.objects.get_or_create(id=8, escolaridad="Magister/Postgrado completo")
    
    Prevision.objects.get_or_create(id=1, prevision="FONASA")
    Prevision.objects.get_or_create(id=2, prevision="Banmédica")
    Prevision.objects.get_or_create(id=3, prevision="Consalud")
    Prevision.objects.get_or_create(id=4, prevision="Colmena")
    Prevision.objects.get_or_create(id=5, prevision="CruzBlanca")
    Prevision.objects.get_or_create(id=6, prevision="Nueva Masvida")
    Prevision.objects.get_or_create(id=7, prevision="Vida Tres")
    Prevision.objects.get_or_create(id=8, prevision="Chuquicamata")
    Prevision.objects.get_or_create(id=9, prevision="Fundación BancoEstado")
    Prevision.objects.get_or_create(id=10, prevision="Fusat")
    Prevision.objects.get_or_create(id=11, prevision="Ríoblanco")
    Prevision.objects.get_or_create(id=13, prevision="SanLorenzo")
    Prevision.objects.get_or_create(id=14, prevision="Cruz del Norte")

    usuario_activo = get_object_or_404(User, pk=request.user.id)

    permiso = EvaluarPermisos(usuario_activo.id)

    if permiso == "es_admin" or permiso == "es_profesional" or permiso == "es_alumno":
        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.password = get_random_string(length=10)
                new_user.save()
                registered = True
                user_paciente = User.objects.latest('id')

                return redirect('registrar_datos_paciente', paciente_id=user_paciente.id)
            else:
                print(user_form.errors)
        else:
            user_form = UserForm()
        context = {
            'user_form': user_form,
            'registered': registered
        }
        return render(request, "registro_paciente.html", context)

    else:
        return render(request, "no_autorizado.html", {})
    
    


@login_required
def registro_datos_paciente_view(request, paciente_id):

    
    usuario_activo = get_object_or_404(User, pk=request.user.id)

    permiso = EvaluarPermisos(usuario_activo.id)

    if permiso == "es_admin" or permiso == "es_profesional" or permiso == "es_alumno":
    
        userPaciente = User.objects.get(id=paciente_id)

        if usuario_activo.is_superuser:
            prof = Profesional.objects.get_or_create(user=usuario_activo, nombre="Administrador")
        else:
            prof = Profesional.objects.get(user=usuario_activo)

        form_paciente = PacienteForm(data=request.POST, prefix='paciente')
        if form_paciente.is_valid():
            paciente = form_paciente.save(commit=False)
            paciente.user = userPaciente
            paciente.profesional = prof
            paciente.save()
        
            send_mail(
                'Bienvenido a la Clinica Virtual',
                'Con este mensaje te damos la bienvenida a nuestro sistema virtual de nutricion, por favor sigue el siguiente link que te dara las instrucciones para establecer una contraseña: http://127.0.0.1:7000/accounts/password_reset/ El equipo de Clinica Virtual',
                'portafolio.clinicavirtual@gmail.com',
                [userPaciente.email],
            )
        
            #se le entrega el permiso de paciente al usuario asignado
            permiso_paciente = Permission.objects.get(name='paciente_permission')
            userPaciente.user_permissions.add(permiso_paciente.id)
        
            return redirect('succes')
        else:
            print(form_paciente.errors)
            print("invalido")
        context = {
            "form_paciente": PacienteForm(prefix='paciente')
        }
        return render(request, "registro_datos_paciente.html", context)

    else:
        return render(request, "no_autorizado.html", {})
    

