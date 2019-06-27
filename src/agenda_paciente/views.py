from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profesional, ControlMedico, Paciente
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from profesional.models import EvaluarPermisos
from .forms import ControlMedicoForm
@login_required
def ver_agenda_view(request):

    usuario_activo = get_object_or_404(User, pk=request.user.id)

    permiso = EvaluarPermisos(usuario_activo.id)

    if permiso == "es_admin" or permiso == "es_profesional" or permiso == "es_alumno" or usuario_activo.is_superuser:

        if usuario_activo.is_superuser:
            prof = Profesional.objects.get_or_create(user=usuario_activo, nombre="Administrador")

            lista_controles = ControlMedico.objects.all()

        else:
            prof = Profesional.objects.get(user=usuario_activo)

            lista_controles = ControlMedico.objects.filter(profesional=prof)

        context = {
            'lista_controles' : lista_controles
        }

        return render(request, "agenda_paciente.html", context)
    else:
        return render(request, "no_autorizado.html", {})
    

@login_required
def agendar_visita_view(request):
    
    usuario_activo = get_object_or_404(User, pk=request.user.id)

    permiso = EvaluarPermisos(usuario_activo.id)

    if permiso == "es_admin" or permiso == "es_profesional" or permiso == "es_alumno" or usuario_activo.is_superuser:

        lista_paciente = Paciente.objects.filter(profesional=usuario_activo)


    
    else:
        return render(request, "no_autorizado.html", {})
    




@login_required
def agendar_datos_visita_view(request):

    usuario_activo = get_object_or_404(User, pk=request.user.id)

    permiso = EvaluarPermisos(usuario_activo.id)

    if permiso == "es_admin" or permiso == "es_profesional" or permiso == "es_alumno" or usuario_activo.is_superuser:
    
        usuario_activo = request.user
        if usuario_activo.is_superuser:
            prof = Profesional.objects.get_or_create(user=usuario_activo, nombre="Administrador")

            lista_controles = ControlMedico.objects.all()

        else:
            prof = Profesional.objects.get(user=usuario_activo)

            lista_controles = ControlMedico.objects.filter(profesional=prof)

        """
        control_form = ControlMedicoForm(request.POST)
        if control_form.is_valid():
            control = control_form.save(commit=False)
            control.profesional = prof
            control.save()
        id_minuta = Minuta.objects.latest('id')
        print(id_minuta)
        return redirect('editar_minuta', id_minuta.id)
        else:
        print(minutaForm)
        return render(request, "registro_minuta.html", {'minutaForm':minutaForm})

        """
        context = {
            'lista_controles' : lista_controles
        }

        return render(request, "agendar_visita.html", context)
    else:
        return render(request, "no_autorizado.html", {})
    

@login_required
def modificar_visita_view(request):

    usuario_activo = get_object_or_404(User, pk=request.user.id)

    permiso = EvaluarPermisos(usuario_activo.id)

    if permiso == "es_admin" or permiso == "es_profesional" or permiso == "es_alumno":
        
        return render(request, "modificar_visita.html", {})

    else:
        return render(request, "no_autorizado.html", {})
