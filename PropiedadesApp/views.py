from django.http import HttpResponse
from django.template import  loader
from django.http import JsonResponse
from PropiedadesApp.service import UsuarioService
from PropiedadesApp.service import ComunaService
from PropiedadesApp.service import PlanContratoService
from PropiedadesApp.service import PropiedadService
from PropiedadesApp.service import TokenService
from django.core import serializers

import requests

from django.conf import settings

def index(request):
    baseurl = request.get_host()
    service_comuna = ComunaService()
    service_comuna.base = baseurl
    resp = service_comuna.get_all()
    if resp['error'] == 0:
        options = {}
        for comuna in resp['data']:
            id = comuna['nid_comuna']
            nombre = comuna['snombre_comuna']
            options[id] = nombre
        context = {'is_public': '1','options':options}
    else:
        context = {'is_public': '1', 'options': ''}
    t = loader.get_template('index.html')
    return HttpResponse(t.render(context))

def propiedades(request):
    t = loader.get_template('propiedad/propiedades.html')
    baseurl = request.get_host()
    service_comuna = ComunaService()
    service_comuna.base = baseurl
    resp = service_comuna.get_all()
    if resp['error'] == 0:
        options = {}
        for comuna in resp['data']:
            id = comuna['nid_comuna']
            nombre = comuna['snombre_comuna']
            options[id] = nombre
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
        context = {'is_public': '1', 'activar_msg': '0', 'error': '0', 'msg': '', 'options': options}
    else:
        context = {'is_public': '1', 'activar_msg': '1', 'error': resp['error'], 'msg': resp['msg'], 'options': ''}
    return HttpResponse(t.render(context))

def detalle(request,propiedad_codigo=None):
    t = loader.get_template('propiedad/detalle.html')
    context = {'list_var': ''}
    return HttpResponse(t.render(context))

def publicar(request):
    t = loader.get_template('propiedad/publicar.html')
    baseurl = request.get_host()
    service_comuna = ComunaService()
    service_comuna.base = baseurl
    resp = service_comuna.get_all()
    if resp['error']==0:
        options = {}
        for comuna in resp['data']:
            id = comuna['nid_comuna']
            nombre = comuna['snombre_comuna']
            options[id] = nombre
        context = {'is_public': '1', 'activar_msg': '0', 'error': '0', 'msg': '', 'options': options}
    else:
        context = {'is_public': '1', 'activar_msg': '1', 'error': resp['error'], 'msg': resp['msg'], 'options': ''}

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
        data = {"tipo": tipo_usuario, "password": clave, "usuario": usuario}
        service.base = request.get_host()
        resp = service.authenticate_user(data)
    return JsonResponse(resp)

def planes(request):
    t = loader.get_template('general/planes.html')
    context = {'list_var': ''}
    return HttpResponse(t.render(context))

def editar_usuario(request):
    t = loader.get_template('usuario/editar_usuario.html')
    baseurl = request.get_host()
    service_comuna = ComunaService()
    service_comuna.base = baseurl
    resp = service_comuna.get_all()
    if resp['error'] == 0:
        options = {}
        for comuna in resp['data']:
            id = comuna['nid_comuna']
            nombre = comuna['snombre_comuna']
            options[id] = nombre
        context = {'activar_msg': '0', 'error': '0', 'msg': '', 'options': options}
    else:
        context = {'activar_msg': '0', 'error': resp['error'], 'msg': resp['msg'], 'options': ''}
    return HttpResponse(t.render(context))

def actualizar_usuario(request):
    baseurl = request.get_host()
    service_usuario = UsuarioService()
    service_usuario.base = baseurl
    if request.is_ajax() and request.method == 'POST':
        #token = request.POST.get('tokenHd')
        token = request.META['HTTP_AUTHORIZATION']
        rut = request.POST.get('txtRut')
        nombre = request.POST.get('txtNombre')
        apellidoP = request.POST.get('txtApellidoP')
        apellidoM = request.POST.get('txtApellidoM')
        direccion = request.POST.get('txtDireccion')
        telefono = request.POST.get('txtTelefono')
        ubicacion = request.POST.get('cmbUbicacion')
        # email = request.POST.get('hdEmail')
        email = request.POST.get('txtEmail')
        email_contacto = request.POST.get('txtEmail')
        opcion_email = request.POST.get('chkOpcion')
        if opcion_email is not None:
            email_contacto = ""
        data = {"id_cuenta": id, "rut": rut, "nombre": nombre, "apellidoP": apellidoP, "apellidoM": apellidoM,
                "direccion": direccion,
                "telefono": telefono, "email": email, 'ubicacion': ubicacion, 'opcion_email': opcion_email,
                "email_contacto": email_contacto, 'token': token}
        service_usuario.set_user(data)
        context = {'error': '0', 'msg': 'Datos guardados correctamente'}
        return JsonResponse(context)

def editar_cuenta(request):
    t = loader.get_template('usuario/editar_cuenta.html')
    context = {'activar_msg': '0', 'error': '0', 'msg': ''}
    return HttpResponse(t.render(context))

def editar_planes(request):
    t = loader.get_template('plan/editar_planes.html')
    context = {'activar_msg': '0', 'error': '0', 'msg': ''}
    return HttpResponse(t.render(context))

def actualizar_cuenta(request):
    if request.is_ajax() and request.method == 'POST':
        service = UsuarioService()
        baseurl = request.get_host()
        service.base = baseurl
        #token = request.POST.get('tokenHd')
        token = request.META['HTTP_AUTHORIZATION']
        actual = request.POST.get('txtClaveActual')
        nuevo1 = request.POST.get('txtClave1')
        nuevo2 = request.POST.get('txtClave2')
        if nuevo1 != nuevo2:
            context = {'error': '1', 'msg': 'Nueva clave ingresada incorrecta'}
        else:
            data = {"clave": actual, "ClaveNueva": nuevo1, 'token': token}
            resp = service.set_account_password(data)
            cod_error = "0"
            msg_error = "Datos guardados correctamente"
            if resp["error"] == "1":
                msg_error = resp["msg"]
                cod_error = "1"
            context = {'error': cod_error, 'msg': msg_error}
        return JsonResponse(context)

def obtener_planes(request):
    service = PlanContratoService()
    service_token = TokenService()
    baseurl = request.get_host()
    service.base = baseurl
    token = request.META['HTTP_AUTHORIZATION']
    param = {"tipo": "1", "token" : token}
    data_token = service_token.decode_token(token)
    if data_token["error"]!="1":
        resp = service.get_all(param)
        context = {'error': '0', 'msg': ''}
        servicio_plan_contrato = 1
        if resp["error"]!="1":
            planes = resp['data']
            #planes["servicio"] = servicio_plan_contrato
            plan_id = int(data_token["plan_id"])
            for item in resp['data']:
                if plan_id == int(item['nid_plan_contrato']):
                    item['plan_actual'] = True
                    break
            context = {'error': '0', 'msg': resp["msg"], 'list': resp['data']}
        else:
            context = {'error': '1', 'msg': resp["msg"]}
    else:
        context = {'error': '1', 'msg': data_token["msg"]}
    return JsonResponse(context)

def obtener_usuario(request):
    service = UsuarioService()
    service.base = request.get_host()
    token = request.META['HTTP_AUTHORIZATION']
    data = {"token": token}
    obj_usuario = service.get_user(data)
    return JsonResponse(obj_usuario)

def editar_datos_comercial(request):
    t = loader.get_template('comercial/editar_comercial.html')
    baseurl = request.get_host()
    service_comuna = ComunaService()
    service_comuna.base = baseurl
    resp = service_comuna.get_all()
    if resp['error'] == 0:
        options = {}
        for comuna in resp['data']:
            id = comuna['nid_comuna']
            nombre = comuna['snombre_comuna']
            options[id] = nombre
        context = {'activar_msg': '0', 'error': '0', 'msg': '', 'options': options}
    else:
        context = {'activar_msg': '0', 'error': resp['error'], 'msg': resp['msg'],'options': ''}
    return HttpResponse(t.render(context))

def publicar_propiedad(request):
    token = request.META['HTTP_AUTHORIZATION']
    if request.is_ajax() and request.method == 'POST':
        service = PropiedadService()
        data = request.POST.dict()
        service.base = request.get_host()
        data.update({'token': token})
        service.add_property(data)
    context = {'error': '0', 'msg': 'Datos guardados correctamente'}
    return JsonResponse(context)

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
            data = {"token": "","username":"" ,"plan":"","plan_id": "",
                    "planLink":"","error": "1", "msg": data_service["msg"],"publico" : publico }
        else:
            data = {"token": data_service["token"],"username":data_service["username"],"error": data_service["error"],
                    "plan":data_service["plan"],"plan_id": data_service["plan_id"],"planLink":data_service["planLink"],
                    "msg": data_service["msg"],"publico" : publico}
    return JsonResponse(data)
