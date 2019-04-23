from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import Context, loader
from django.http import JsonResponse
from Api.service import UsuarioService
import requests,json
from PropiedadesApp.models import CuentaAcceso
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
        data = {"tipo": tipo_usuario,"password": clave,"usuario": usuario}
        baseurl = request.get_host()
        request_service = requests.post(url = "http://" + baseurl +"/api/authenticate_user/", data = data )
        data_service = request_service.json()
        if data_service["error"]==1:
            data = {"token": "", "error": "1", "msg": data_service["msg"],"username" :"" }
        else:
            data = {"token": data_service["token"],"error":0, "msg": data_service["msg"], "username" :data_service["username"] }
    return JsonResponse(data)

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
    context = {'is_public': '0'}
    return HttpResponse(t.render(context))

def editar_cuenta(request):
    t = loader.get_template('usuario/editar_cuenta.html')
    context = {'is_public': '0'}
    return HttpResponse(t.render(context))