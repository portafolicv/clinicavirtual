from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesional, Minuta, Receta, RecetaEnMinuta
from .forms import MinutaForm, RecetaEnMinutaForm
from django.contrib.auth.decorators import login_required



#falta docu
@login_required
def buscar_minuta_view(request):
    usuario_activo = request.user
    if usuario_activo.is_superuser:
        prof = Profesional.objects.get_or_create(user=usuario_activo, nombre="Administrador")
        list_minutas = Minuta.objects.all().order_by('id')
    else:
        prof = Profesional.objects.get(user=usuario_activo)
        list_minutas = Minuta.objects.filter(profesional=prof).order_by('id')

    return render(request, "buscar_minuta.html", {'list_minutas' : list_minutas})



#falta docu
@login_required
def registro_minuta_view(request):
    usuario_activo = request.user
    if usuario_activo.is_superuser:
        prof = Profesional.objects.get_or_create(user=usuario_activo, nombre="Administrador")
    else:
        prof = Profesional.objects.get(user=usuario_activo)

    minutaForm = MinutaForm(request.POST)
    if minutaForm.is_valid():
        minuta = minutaForm.save(commit=False)
        minuta.profesional = prof
        minuta.save()
        id_minuta = Minuta.objects.latest('id')
        print(id_minuta)
        return redirect('editar_minuta', id_minuta.id)
    else:
        print(minutaForm)
        return render(request, "registro_minuta.html", {'minutaForm':minutaForm})


#falta docu
@login_required
def editar_minuta_view(request, id_minuta):

    minuta_edit = Minuta.objects.get(id=id_minuta)
    
    list_recetaminuta = RecetaEnMinuta.objects.filter(minuta=minuta_edit)
    
    form_recetaenminuta = RecetaEnMinutaForm(request.POST)
    if form_recetaenminuta.is_valid():
        f_rm = form_recetaenminuta.save(commit=False)
        f_rm.minuta = minuta_edit
        f_rm.save()
        return redirect('editar_minuta', id_minuta)
    
    context = {
        'minuta_edit' : minuta_edit,
        'list_recetaminuta' : list_recetaminuta,
        'form_recetaenminuta' : form_recetaenminuta
    }
    return render(request, "edit_minuta.html", context)


 #falta docu   
@login_required
def remover_minuta_view(request, id_minuta):
    minuta_remov = get_object_or_404(Minuta, id=id_minuta)
    minuta_remov.delete()
    return redirect('buscar_minuta')



#falta docu
@login_required
def remover_recetaenminuta_view(request, id_recetaenminuta, id_minuta):
    recetaenminuta_remov = get_object_or_404(RecetaEnMinuta, id=id_recetaenminuta)
    recetaenminuta_remov.delete()
    return redirect('editar_minuta', id_minuta)