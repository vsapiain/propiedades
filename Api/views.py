from rest_framework import permissions,status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from Api.service import UsuarioService
from Api.service import ComunaService
from Api.service import  PlanService
from Api.service import PropiedadService
from Api.service import PublicacionService
from Api.service import  TokenService

@api_view (['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    if request.method == 'POST':
        service = UsuarioService()
        tipo_usuario = request.data['tipo']
        password = request.data['password']
        usuario = request.data['usuario']
        if tipo_usuario == "1":
            data = service.is_authenticated_particular(usuario,password)
        else:
            if tipo_usuario == "2":
                data = service.is_authenticated_corredora(usuario,password)
            else:
                data = service.is_authenticated_inmobiliaria(usuario, password)
        if data["token"] != "":
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

@api_view (['GET','PUT'])
@permission_classes([AllowAny, ])
def users(request,id=None):
    token = request.META['HTTP_AUTHORIZATION']
    service_token = TokenService()
    token_data = service_token.decode_token(token)
    if token_data["error"] == "0":
        service = UsuarioService()
        if request.method == 'GET':
            data = service.get_user_detail(id)
            return Response(data, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            rut = request.POST.get('rut')
            nombre = request.POST.get('nombre')
            apellidoP = request.POST.get('apellidoP')
            apellidoM = request.POST.get('apellidoM')
            direccion = request.POST.get('direccion')
            telefono = request.POST.get('telefono')
            email = request.POST.get('email')
            ubicacion = request.POST.get('ubicacion')
            opcion_email = request.POST.get('opcion_email')
            email_contacto = request.POST.get('email_contacto')
            data = {"rut": rut, "nombre": nombre, "apellidoP": apellidoP, "apellidoM": apellidoM,
            "direccion": direccion,"telefono": telefono, "email": email,"opcion_email":opcion_email,"email_contacto":email_contacto,'ubicacion':ubicacion, 'token': token}
            data = service.update_user(id,data)
            if data["error"]=="0":
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(token_data, status=status.HTTP_401_UNAUTHORIZED)

@api_view (['PUT'])
@permission_classes([AllowAny, ])
def account(request,id=None):
    token = request.META['HTTP_AUTHORIZATION']
    service_token = TokenService()
    token_data = service_token.decode_token(token)
    if token_data["error"] == "0":
        service = UsuarioService()
        if request.method == 'PUT':
            usuario = request.POST.get('usuario')
            FVigenciaInicial = request.POST.get('FInicial')
            FVigenciaFinal = request.POST.get('FFinal')
            email = request.POST.get('email')
            clave = request.POST.get('clave')
            data ={"usuario":usuario,"email":email,"FVigeniaInicial":FVigenciaInicial,"FVigenciaFinal":FVigenciaFinal,"clave":clave}
            data = service.update_account(id, data)
            return Response(token_data, status=status.HTTP_200_OK)
    else:
        return Response(token_data, status=status.HTTP_401_UNAUTHORIZED)

@api_view (['GET','POST'])
@permission_classes([AllowAny, ])
def get_communes(request):
    service = ComunaService()
    resp = service.get_all()
    if resp['error']==1:
        return Response(resp, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(resp, status=status.HTTP_200_OK)

@api_view (['GET'])
@permission_classes([AllowAny, ])
def get_plans(request):
    token = request.META['HTTP_AUTHORIZATION']
    tipo_plan = request.GET['tipo']
    service_token = TokenService()
    token_data = service_token.decode_token(token)
    if token_data["error"] == "0":
        service = PlanService()
        if tipo_plan == "1":
            data = service.get_all_particular()
        else:
            if tipo_plan == "2":
                pass
            else:
                pass
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response(token_data, status=status.HTTP_401_UNAUTHORIZED)

@api_view (['GET','POST'])
@permission_classes([AllowAny, ])
def property(request):
    token = request.META['HTTP_AUTHORIZATION']
    service_token = TokenService()
    token_data = service_token.decode_token(token)
    if token_data["error"] == "0":
        propiedad_service = PropiedadService()
        if request.method == 'POST':
            registro_activo = 1
            quincho = 1 if request.POST.get('Quincho') is not None else -1
            gimnasio = 1 if request.POST.get('Gimnasio') is not None else -1
            lavanderia = 1 if request.POST.get('Lavandería') is not None else -1
            piscina = 1 if request.POST.get('Piscina') is not None else -1
            bodega = 1 if request.POST.get('Bodega') is not None else -1
            tipo_propiedad = request.POST.get('cmbTipoPropiedad')
            operacion = request.POST.get('cmbOperacion')
            titulo = request.POST.get('txtTitulo')
            descripcion = request.POST.get('txtDescripcion')
            area_total = request.POST.get('ddl_area_filter')
            direccion = request.POST.get('txtDireccion')
            ubicacion = request.POST.get('cmbUbicacion')
            dormitorio = request.POST.get('cmbDormitorio')
            banno = request.POST.get('cmbBanno')
            estacionamiento = request.POST.get('cmbEstacion amiento')
            codigo = 1
            propiedad_instance = propiedad_service.save(codigo,tipo_propiedad,direccion,
                         ubicacion,dormitorio,banno,estacionamiento,-1,area_total,-1,quincho,-1,gimnasio,lavanderia,-1,-1,-1,-1,
                         -1,piscina,-1,-1,-1,bodega,None,None,registro_activo)
            if propiedad_instance is not None:
                publicacion_service = PublicacionService()
                publicacion_service.save(propiedad_instance.nid_propiedad,token_data['plan_id'],token_data['id'],
                                         operacion,titulo,descripcion,None,None,'',registro_activo)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(token_data, status=status.HTTP_401_UNAUTHORIZED)

@api_view (['GET','POST'])
@permission_classes([AllowAny, ])
def verify_token(request):
    try:
        token = request.META['HTTP_AUTHORIZATION']
        service = TokenService()
        token_data = service.decode_token(token)
        return Response(token_data,status=status.HTTP_200_OK)
    except Exception as err:
        return Response(token_data,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
