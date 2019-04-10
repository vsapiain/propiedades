from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import Context, loader
from django.http import JsonResponse
from Api.service import usuario_service
#from PropiedadesApp.service import usuario_service
import requests,json
from PropiedadesApp.models import CuentaAcceso

def index(request):
    '''
    user_ = Usuario(Clave='123', Email='XXX')
    user_.save()
    '''
    '''
    token = request.session.get('token', '')
    request.META['HTTP_AUTHORIZATION'] = token
    respuesta = json.loads(verificar_usuario(request).content.decode())
    activa = '0'
    if respuesta['error']!=1 and token is not None and token!='':
        activa = '1'
    '''
    token = request.session.get('token', '')
    request.META['HTTP_AUTHORIZATION'] = token
    respuesta = json.loads(verificar_usuario(request).content.decode())
    estado_login = '0'
    if respuesta['error'] != 1:
        estado_login = '1'
    context = {'authenticated': estado_login}
    t = loader.get_template('index.html')
    return HttpResponse(t.render(context))

def propiedades(request):
    t = loader.get_template('propiedades.html')
    context = {'list_var': ''}
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
    t = loader.get_template('detalle.html')
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
        service = usuario_service()
        data = {"tipo": tipo_usuario,"password": clave,"usuario": usuario}
        baseurl = request.get_host()
        request_service = requests.post(url = "http://" + baseurl +"/api/authenticate_user/", data = data )
        data_service = request_service.json()
        if data_service["error"]==1:
            data = {"token": "", "error": "1", "msg": data_service["msg"],"username" :"" }
        else:
            request.session['token'] = data_service["token"]
            data = {"token": data_service["token"],"error":0, "msg": data_service["msg"], "username" :data_service["username"] }
    return JsonResponse(data)

def planes(request):
    t = loader.get_template('planes.html')
    context = {'list_var': ''}
    return HttpResponse(t.render(context))

def verificar_usuario(request):
    data = ''
    if request.method == "GET":
        token = ''
        if request.META.get('HTTP_AUTHORIZATION') is not None:
            token = request.META['HTTP_AUTHORIZATION']
        baseurl = request.get_host()
        headers = {'Authorization': token}
        request_service = requests.post(url="http://" + baseurl + "/api/verify_token/", data=token, headers=headers)
        data_service = request_service.json()
        if data_service["error"]=="1":
            data = {"token": "", "error": "1", "msg": data_service["msg"]}
        else:
            data = {"token": data_service["token"],"error": data_service["error"],"msg": data_service["msg"]}
            request.session['token'] = data_service["token"]

    return JsonResponse(data)