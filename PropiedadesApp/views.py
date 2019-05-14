from django.http import HttpResponse
from django.template import  loader
from django.http import JsonResponse
from PropiedadesApp.service import UsuarioService
from PropiedadesApp.service import ComunaService
import requests
from django.core import serializers
import json

from django.conf import settings

def index(request):
    '''
    user_ = Usuario(Clave='123', Email='XXX')
    user_.save()
    '''
    context = {'is_public': '1'}
    t = loader.get_template('index.html')
    return HttpResponse(t.render(context))

def propiedades(request):
    t = loader.get_template('propiedad/propiedades.html')
    context = {'is_public': '1'}
    if request.method == "POST":
        filter_modo = request.POST.get("cmb_operacion_portada")
        filte_tipo = request.POST.get("cmb_tipo_propiedad_portada")
        filter_ubicacion = request.POST.get("cmb_ubicacion_portada")
        filter_precio_min = request.POST.get("min-price")
        filter_precio_max = request.POST.get("max-price")
        filter_size_min = request.POST.get("min-size")
        filter_size_max = request.POST.get("max-size")
        filter_dormitorio = request.POST.get("n_dormitorios_otros")
        filter_bano = request.POST.get("n_banos_otros")
        filter_estacionamientos = request.POST.get("n_estacionamientos_otros")

    context = {'list_var': ''}
    return HttpResponse(t.render(context))

def detalle(request,propiedad_codigo=None):
    t = loader.get_template('propiedad/detalle.html')
    context = {'list_var': ''}
    return HttpResponse(t.render(context))

def login(request):
    t = loader.get_template('index.html')
    msg = ""
    data = {"token": "", "msg": "", "username": ""}
    if request.method == 'POST':
        usuario = request.POST.get("data[0][value]")
        clave = request.POST.get("data[1][value]")
        tipo_usuario = request.POST.get("data[2][value]")
        service = UsuarioService()
        #baseurl = request.get_host()
        data = {"tipo": tipo_usuario, "password": clave, "usuario": usuario}
        service.base = request.get_host()
        resp = service.authenticate_user(data)
    return JsonResponse(resp)

def planes(request):
    t = loader.get_template('general/planes.html')
    context = {'list_var': ''}
    return HttpResponse(t.render(context))

def verificar_usuario(request):
    data = ''
    if request.method == "GET":
        token = ''
        url = ''
        i=1
        for item in request.META.get('HTTP_REFERER').split("/")[3:]:
            if i==1:
                url = item
            else:
                url = url + "/" + item
            i+=1
        url = url.split("?")[0]
        publico = "1"
        if url in settings.PAGE_PATH_IS_NOT_PUBLIC:
            publico  = "0"

        if request.META.get('HTTP_AUTHORIZATION') is not None:
            token = request.META['HTTP_AUTHORIZATION']
        baseurl = request.get_host()
        headers = {'Authorization': token}
        request_service = requests.post(url="http://" + baseurl + "/api/verify_token/", data=token, headers=headers)
        data_service = request_service.json()
        if data_service["error"]=="1":
            data = {"token": "","username":"" ,"error": "1", "msg": data_service["msg"],"publico" : publico }
        else:
            data = {"token": data_service["token"],"username":data_service["username"],"error": data_service["error"],"msg": data_service["msg"],"publico" : publico}
    return JsonResponse(data)

def editar_usuario(request):
    t = loader.get_template('usuario/editar_usuario.html')
    baseurl = request.get_host()
    service_usuario = UsuarioService()
    service_usuario.base = baseurl
    service_comuna = ComunaService()
    service_comuna.base = baseurl
    comunas = service_comuna.get_all()
    options ={}
    obj_comunas = serializers.deserialize('json', comunas["obj"])
    for comuna in obj_comunas:
        id = comuna.object.nid_comuna
        nombre = comuna.object.snombre_comuna
        options[id]=nombre
    context = {'activar_msg': '0', 'error': '0', 'msg': '', 'options': options}
    if request.method == 'POST':
        token = request.POST.get('tokenHd')
        #decode_tkn = service.decode_token(token)
        rut = request.POST.get('txtRut')
        nombre = request.POST.get('txtNombre')
        apellidoP = request.POST.get('txtApellidoP')
        apellidoM = request.POST.get('txtApellidoM')
        direccion = request.POST.get('txtDireccion')
        telefono = request.POST.get('txtTelefono')
        ubicacion = request.POST.get('cmbUbicacion')
        #email = request.POST.get('hdEmail')
        email = request.POST.get('txtEmail')
        email_contacto = request.POST.get('txtEmail')
        opcion_email = request.POST.get('chkOpcion')
        if opcion_email is not None:
            email_contacto = ""

        data = {"id_cuenta":id,"rut": rut, "nombre": nombre , "apellidoP":apellidoP,"apellidoM":apellidoM,"direccion":direccion,
                "telefono":telefono,"email":email,'ubicacion':ubicacion,'opcion_email':opcion_email,"email_contacto":email_contacto,'token':token}
        service_usuario.set_user(data)
        context = {'activar_msg': '1','error':'0', 'msg': 'Datos guardados correctamente','options':options}
    return HttpResponse(t.render(context))

def editar_cuenta(request):
    t = loader.get_template('usuario/editar_cuenta.html')
    context = {'activar_msg': '0', 'error': '0', 'msg': ''}
    if request.method == 'POST':
        service = UsuarioService()
        baseurl = request.get_host()
        service.base = baseurl
        token = request.POST.get('tokenHd')
        actual = request.POST.get('txtClaveActual')
        nuevo1 = request.POST.get('txtClave1')
        nuevo2 = request.POST.get('txtClave2')
        if nuevo1 != nuevo2:
            context = {'activar_msg': '1', 'error': '1', 'msg': 'Nueva clave ingresada incorrecta'}
        else:
            data = {"clave":actual,"ClaveNueva":nuevo1,'token':token}
            resp = service.set_account_password(data)
            cod_error = "0"
            msg_error = ""
            if resp["error"]=="1":
                msg_error = resp["msg"]
                cod_error = "1"
            context = {'activar_msg': '1', 'error': cod_error, 'msg': msg_error}


    return HttpResponse(t.render(context))

def obtener_usuario(request):
    service = UsuarioService()
    service.base = request.get_host()
    token = request.META['HTTP_AUTHORIZATION']
    data = {"token": token}
    obj_usuario = service.get_user(data)
    context = {'object': obj_usuario}
    return JsonResponse(obj_usuario)

def obtener_comunas(request):
    if request.is_ajax():
        service = ComunaService()
        service.base = request.get_host()
        comunas  =  service.get_all()
        return JsonResponse(comunas)
