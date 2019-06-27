from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesional, Alimento, Receta, AlimentoEnReceta, TipoServicioReceta
from registro_alimento.models import Proteina, HidratoC, Vitamina, Lipido, Mineral
from registro_alimento.models import VitaminaAlimento, HidratoCAlimento, ProteinaAlimento, LipidoAlimento, MineralAlimento
from .forms import RecetaForm, AlimentoEnRecetaForm
from django.contrib.auth.decorators import login_required


#falta docu
@login_required
def buscar_receta_view(request):

    usuario_activo = request.user

    if usuario_activo.is_superuser:
        prof = Profesional.objects.get_or_create(user=usuario_activo, nombre="Administrador")
        recetas = Receta.objects.all().order_by('id')
    else:
        prof = Profesional.objects.get(user=usuario_activo)
        recetas = Receta.objects.filter(profesional = prof).order_by('id')

    return render(request, "buscar_receta.html", {"recetas":recetas})


#falta docu
@login_required
def remover_receta_view(request, id_rc):
    rc = Receta.objects.get(id=id_rc)
    rc.delete()
    return redirect('buscar_receta')


#falta docu
@login_required
def registro_receta_view(request):

    usuario_activo = request.user
    if usuario_activo.is_superuser:
        prof = Profesional.objects.get_or_create(user=usuario_activo, nombre="Administrador")
    else:
        prof = Profesional.objects.get(user=usuario_activo)

    TipoServicioReceta.objects.get_or_create(id=1, tipo="Desayuno")
    TipoServicioReceta.objects.get_or_create(id=2, tipo="Media mañana")
    TipoServicioReceta.objects.get_or_create(id=3, tipo="Almuerzo")
    TipoServicioReceta.objects.get_or_create(id=4, tipo="Merienda")
    TipoServicioReceta.objects.get_or_create(id=5, tipo="Cena")

    form_receta = RecetaForm(request.POST)
    if form_receta.is_valid():
        receta = form_receta.save(commit=False)
        receta.profesional = prof
        receta.save()
        id_rc = Receta.objects.latest('id')
        return redirect('editar_receta', id_rc.id)
    else:
        return render(request, "registro_receta.html", {"form_receta": form_receta})



#falta docu
@login_required
def editar_receta_view(request, id_rc):

    receta_edit = Receta.objects.get(id=id_rc)

    preparacion_receta = receta_edit.preparacion
    
    list_alimentoenreceta = AlimentoEnReceta.objects.filter(receta=receta_edit)
    
    form_alimentoReceta = AlimentoEnRecetaForm(request.POST)
    if form_alimentoReceta.is_valid():
        f_ar = form_alimentoReceta.save(commit=False)
        f_ar.receta = receta_edit
        f_ar.save()
        return redirect('editar_receta', id_rc)
    
    if 'btn_preparacion' in request.POST:
        receta_editar = get_object_or_404(Receta, id=id_rc)
        if request.method == "POST":
                receta_editar.preparacion = request.POST.get("preparacion_receta")
                receta_editar.save()
                return redirect('editar_receta', id_rc)

    context = {
        'receta_edit' : receta_edit,
        'list_alimentoenreceta' : list_alimentoenreceta,
        'preparacion_receta' : preparacion_receta,
        'form_alimentoReceta' : form_alimentoReceta
    }
    return render(request, "edit_receta.html", context)



#falta docu
@login_required
def remover_alimentoenreceta_view(request, id_alimentoenreceta, id_rc):

    remover_alrc = get_object_or_404(AlimentoEnReceta, id=id_alimentoenreceta)
    remover_alrc.delete()
    return redirect('editar_receta', id_rc)