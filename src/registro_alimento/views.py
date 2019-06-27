from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import AlimentoForm, VitaminaForm, MineralForm, LipidoForm, ProteinaForm, HidratoCForm
from .forms import VitaminaAlimentoForm, MineralAlimentoForm, LipidoAlimentoForm, ProteinaAlimentoForm, HidratoCAlimentoForm
from .models import Profesional, Alimento, Proteina, HidratoC, Vitamina, Lipido, Mineral
from .models import VitaminaAlimento, HidratoCAlimento, ProteinaAlimento, LipidoAlimento, MineralAlimento, Unidad_Medida, Envase
from django.contrib.auth.decorators import login_required


#ok
@login_required
def buscar_alimento_view(request):
    
    """
    Función buscar_alimento:
    Esta funcion es la primera vista referia a los alimentos en el sistema. 
    Su objetivo es tomar todos los alimentos creados por el usuario del tipo profesional conectado (sea o no alumno), y listarlos en el template. 
    Requiere que el usuario inicie sesion en el sistema.    
    """

    usuario_activo = request.user
    if usuario_activo.is_superuser:
        alimentos = Alimento.objects.all()
    else:
        prof = Profesional.objects.get(user = usuario_activo)
        alimentos = Alimento.objects.filter(profesional = prof)

    return render(request, "buscar_alimento.html", {"alimentos" : alimentos})


#ok
@login_required
def registro_alimento_view(request):

    """
    Función registro_alimento:
    Esta función es la encargada de crear los alimentos en la base de datos.
    Para ello captura la informacion del usuario profesional activo, y con ello completa el formularion del alimento.
    Requiere que el usuario inicie sesion en el sistema.    
    """

    usuario_activo = request.user
    if usuario_activo.is_superuser:
        prof = Profesional.objects.get_or_create(user=usuario_activo, nombre="Administrador")
    else:
        prof = Profesional.objects.get(user=usuario_activo)
    
    #verificacion de los objetos para el llenado de la tabla de unidad de medida
    Unidad_Medida.objects.get_or_create(id=1, unidad_medida="Kilogramo")
    Unidad_Medida.objects.get_or_create(id=2, unidad_medida="Miligramo")
    Unidad_Medida.objects.get_or_create(id=3, unidad_medida="Litro")
    Unidad_Medida.objects.get_or_create(id=4, unidad_medida="Mililitro")
    
    #verificacion de los objetos para el llenado de la tabla de envase
    Envase.objects.get_or_create(id=1, envase="venta a granel")
    Envase.objects.get_or_create(id=2, envase="caja de cartón")
    Envase.objects.get_or_create(id=3, envase="bolsa de papel")
    Envase.objects.get_or_create(id=4, envase="bolsa plastica")
    Envase.objects.get_or_create(id=5, envase="envase plastico")
    Envase.objects.get_or_create(id=6, envase="botella de vidrio")
    Envase.objects.get_or_create(id=7, envase="botella plastica")
    Envase.objects.get_or_create(id=8, envase="conserva metalica")

    #creacion del objeto alimento
    form_alimento = AlimentoForm(request.POST)
    if form_alimento.is_valid():
        alimento = form_alimento.save(commit=False)
        alimento.profesional = prof
        alimento.save()
        id_al = Alimento.objects.latest('id')
        return redirect('editar_alimento', id_al.id)
    else:
        return render(request, "registro_alimento.html", {"form_alimento": AlimentoForm})


#ok
@login_required
def editar_alimento_view(request, id_al):

    """
    Función editar_alimento:
    Esta función se encarga de agregar los componentes que conforman el alimento. 
    Trabaja con multiples formularios al mismo tiempo, por lo que su flujo es gestionado por distintas condicionales que permiten trabajar cada clase por separado.
    Requiere que el usuario inicie sesion en el sistema. 
    """

    al_edit = Alimento.objects.get(id=id_al)
    unidad_med = Unidad_Medida.objects.get(id=2)
    proteina = Proteina.objects.get_or_create(id=1, nombre='Proteina', unidad_medida=unidad_med)
    hidratoc = HidratoC.objects.get_or_create(id=1, nombre='Hidrato de Carbono', unidad_medida=unidad_med)

    qs_vit_al = []
    qs_hid_al = []
    qs_pro_al = []
    qs_lip_al = []
    qs_min_al = []

  
    qs_vit_al = VitaminaAlimento.objects.filter(alimento = al_edit)
    qs_hid_al = HidratoCAlimento.objects.filter(alimento = al_edit)
    qs_pro_al = ProteinaAlimento.objects.filter(alimento = al_edit)
    qs_lip_al = LipidoAlimento.objects.filter(alimento = al_edit)
    qs_min_al = MineralAlimento.objects.filter(alimento = al_edit)

    
    if 'btn_vitamina' in request.POST:
        form_vitamina = VitaminaForm(request.POST, prefix='vitamina')
        if form_vitamina.is_valid():
            form_vitamina.save()

    if 'btn_vitaminaAlimento' in request.POST:
        form_vitaminaAlimento = VitaminaAlimentoForm(request.POST, prefix='vitaminaAlimento')
        if form_vitaminaAlimento.is_valid():
            vit_al= form_vitaminaAlimento.save(commit=False)
            vit_al.alimento = al_edit
            vit_al.save()
            return redirect('editar_alimento', al_edit.id)
    
    if 'btn_mineral' in request.POST:
        form_mineral = MineralForm(request.POST, prefix='mineral')
        if form_mineral.is_valid():
            form_mineral.save()

    if 'btn_mineralAlimento' in request.POST:
        form_mineralAlimento = MineralAlimentoForm(request.POST, prefix='mineralAlimento')
        if form_mineralAlimento.is_valid():
            min_al= form_mineralAlimento.save(commit=False)
            min_al.alimento = al_edit
            min_al.save()
            return redirect('editar_alimento', al_edit.id)
    
    if 'btn_lipido' in request.POST:
        form_lipido = LipidoForm(request.POST, prefix='lipido')
        if form_lipido.is_valid():
            form_lipido.save()

    if 'btn_lipidoAlimento' in request.POST:
        form_lipidoAlimento = LipidoAlimentoForm(request.POST, prefix='lipidoAlimento')
        if form_lipidoAlimento.is_valid():
            lip_al = form_lipidoAlimento.save(commit=False)
            lip_al.alimento = al_edit
            lip_al.save()
            return redirect('editar_alimento', al_edit.id)

    if 'btn_proteinaAlimento' in request.POST:
        form_proteinaAlimento = ProteinaAlimentoForm(request.POST, prefix='proteinaAlimento')
        if form_proteinaAlimento.is_valid():
            pro_al = form_proteinaAlimento.save(commit=False)
            pro_al.proteina = proteina
            pro_al.alimento = al_edit
            pro_al.save()
            return redirect('editar_alimento', al_edit.id)         

    if 'btn_hidratoAlimento' in request.POST:
        form_hidratoCAlimento = HidratoCAlimentoForm(request.POST, prefix='hidratoAlimento')
        if form_hidratoCAlimento.is_valid():
            hid_al = form_hidratoCAlimento.save(commit=False) 
            hid_al.hidratoC = hidratoc
            hid_al.alimento = al_edit
            hid_al.save()
            return redirect('editar_alimento', al_edit.id)
    

    context = {
        "al_edit"               : al_edit,
        "qs_vit_al"             : qs_vit_al,
        "qs_hid_al"             : qs_hid_al,
        "qs_pro_al"             : qs_pro_al,
        "qs_lip_al"             : qs_lip_al,
        "qs_min_al"             : qs_min_al,
        "form_vitamina"         : VitaminaForm(prefix='vitamina'),
        "form_mineral"          : MineralForm(prefix='mineral'),
        "form_lipido"           : LipidoForm(prefix='lipido'),
        "form_vitaminaAlimento" : VitaminaAlimentoForm(prefix='vitaminaAlimento'),
        "form_mineralAlimento"  : MineralAlimentoForm(prefix='mineralAlimento'),
        "form_lipidoAlimento"   : LipidoAlimentoForm(prefix='lipidoAlimento'),
        "form_proteinaAlimento" : ProteinaAlimentoForm(prefix='proteinaAlimento'),
        "form_hidratoCAlimento" : HidratoCAlimentoForm(prefix='hidratoAlimento')
    }


    return render(request, "edit_alimento.html", context)


#ok
@login_required
def rm_alimento_view(request, id_al):

    """
    Función rm_alimento:
    Esta función se encarga de eliminar los alimentos, lo que genera que los componentes tambien se borren de la base de datos.
    Requiere que el usuario inicie sesion en el sistema. 
    """

    alimentoaeliminar = get_object_or_404(Alimento, id=id_al)
    alimentoaeliminar.delete()
    return redirect('buscar_alimento')


#ok
@login_required
def rm_componente_view(request, id_al, tipo, id_comp):

    """
    Funcion rm_componente:
    Se encarga de eliminar los componentes de alimento sin eliminar el alimento mismo.
    para ello primero identifica el tipo de componente a través parametros.
    Requiere que el usuario inicie sesion en el sistema. 
    """

    if tipo == 0:
        cp = get_object_or_404(VitaminaAlimento, id=id_comp)
        cp.delete()
        return redirect('editar_alimento', id_al)

    if tipo == 2:
        cp = get_object_or_404(ProteinaAlimento, id=id_comp)
        cp.delete()
        return redirect('editar_alimento', id_al)

    if tipo == 3:
        cp = get_object_or_404(LipidoAlimento, id=id_comp)
        cp.delete()
        return redirect('editar_alimento', id_al)
    
    if tipo == 1:
        cp = get_object_or_404(HidratoCAlimento, id=id_comp)
        cp.delete()
        return redirect('editar_alimento', id_al)
    
    if tipo == 4:
        cp = get_object_or_404(MineralAlimento, id=id_comp)
        cp.delete()
        return redirect('editar_alimento', id_al)