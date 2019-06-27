from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from profesional.forms import UserForm, ProfesionalForm
from profesional.models import Profesional, EvaluarPermisos, User
from gestion_paciente.models import Paciente
from django.contrib.contenttypes.models import ContentType
from django.utils.crypto import get_random_string
from django.core.mail import send_mail





#login del sistema

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                
                return HttpResponseRedirect(reverse('charge'))

            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        print("este es el login que estas usando")
        return render(request, 'login.html', {})


#vistas adicionales al login
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('welcome'))


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_charge(request):
    usuario_activo = request.user

    if usuario_activo: 
        return HttpResponseRedirect(reverse('home'))



########  VISTAS PARA LA CREACION DE PROFESONALES Y ALUMNOS  #########

@login_required
def registrar_profesional_view(request):

    usuario_activo = get_object_or_404(User, pk=request.user.id)

    permiso = EvaluarPermisos(usuario_activo.id)

    if permiso == "es_admin" or permiso == "es_profesional" or usuario_activo.is_superuser:

        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.password = get_random_string(length=10)
                new_user.save()
                registered = True

                user_profesional = User.objects.latest('id')

                return redirect('registrar_datos_profesional', profesional_id=user_profesional.id)

            else:
                print(user_form.errors)
        else:
            user_form = UserForm()
        context = {
            'user_form': user_form,
            'registered': registered
        }
        return render(request, "registro_profesional.html", context)
    else:
        return render(request, "no_autorizado.html", {})
    

@login_required
def registrar_datos_profesional_view(request, profesional_id):

    
    usuario_activo = get_object_or_404(User, pk=request.user.id)

    permiso = EvaluarPermisos(usuario_activo.id)

    if permiso == "es_admin" or permiso == "es_profesional" or usuario_activo.is_superuser:
    
        user_profesional = User.objects.get(id=profesional_id)

        
        form_profesional = ProfesionalForm(data=request.POST, prefix='profesional')
        if form_profesional.is_valid():
            profesional = form_profesional.save(commit=False)
            profesional.user = user_profesional
            if usuario_activo.is_superuser:
                var =  request.POST.get("cbx_es_alumno", False)
                if var:
                    profesional.es_alumno = True
                else:
                    profesional.es_alumno = False

            profesional.save()
        
            send_mail(
                'Bienvenido a la Clinica Virtual',
                'Con este mensaje te damos la bienvenida a nuestro sistema virtual de nutricion, por favor sigue el siguiente link que te dara las instrucciones para establecer una contraseña: http://127.0.0.1:7000/accounts/password_reset/ El equipo de Clinica Virtual',
                'portafolio.clinicavirtual@gmail.com',
                [user_profesional.email],
            )
        
            #se le entrega el permiso de profesional al usuario asignado
            if profesional.es_alumno:
                permiso_profesional = Permission.objects.get(name='alumno_permission')
            else:
                permiso_profesional = Permission.objects.get(name='profesional_permission')

            user_profesional.user_permissions.add(permiso_profesional.id)
                
            return redirect('succes')
        else:
            print(form_profesional.errors)
            print("invalido")
        context = {
            "form_profesional": ProfesionalForm(prefix='profesional')
        }
        return render(request, "registro_datos_profesional.html", context)

    else:
        return render(request, "no_autorizado.html", {})
    

