from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import Context, loader
from django.http import JsonResponse

from PropiedadesApp.models.usuario_model import Usuario
from PropiedadesApp.proxy.usuario_proxy import  usuario_proxy
from PropiedadesApp.service.usuario_service import  usuario_service




# Create your views here.
def index(request):

    '''
    user_ = Usuario(Clave='123', Email='XXX')
    user_.save()
    '''

    '''
    user_ = Usuario()
    user_obj =  user_.get(22)
    user_obj.update(Email='email_prueba');
    '''

    '''
    user_ = Usuario()
    user_obj = user_.get(22)
    user_obj.delete()
    '''

    '''
    proxy_  = usuario_proxy.usuario_proxy()
    usuario_1 = proxy_.get(23)
    usuario_2 = proxy_.get_by_email('admin@gmail.com')
    '''

    #service = usuario_service()
    #resultado = service.is_authenticated('admin@gmail.co',12)

    t = loader.get_template('index.html')
    context = {'list_var': ''}
    return HttpResponse(t.render(context))

def propiedades(request):
    t = loader.get_template('propiedades.html')
    context = {'list_var': ''}
    if request.method == "POST":
        filter_modo = request.POST.get("cmb_modo_portada")
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
    usuario = request.GET['username']
    clave = request.GET['password']
    service = usuario_service()
    resultado,msg = service.is_authenticated(usuario,clave)
    data = {'is_authenticated': resultado.authenticated, 'msg': msg}
    return JsonResponse(data)

