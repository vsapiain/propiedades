from rest_framework import permissions,status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from Api.service import UsuarioService
from Api.service import ComunaService

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
    try:
        token = request.META['HTTP_AUTHORIZATION']
        service = UsuarioService()
        token_data = service.decode_token(token)
        if token_data["error"] == "0":
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
    except ValueError:
        return Response(token_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view (['PUT'])
@permission_classes([AllowAny, ])
def account(request,id=None):
    try:
        token = request.META['HTTP_AUTHORIZATION']
        service = UsuarioService()
        token_data = service.decode_token(token)
        if token_data["error"] == "0":
            if request.method == 'PUT':
                usuario = request.POST.get('usuario')
                FVigenciaInicial = request.POST.get('FInicial')
                FVigenciaFinal = request.POST.get('FFinal')
                email = request.POST.get('email')
                clave = request.POST.get('clave')
                data ={"usuario":usuario,"email":email,"FVigeniaInicial":FVigenciaInicial,"FVigenciaFinal":FVigenciaFinal,"clave":clave}
                data = service.update_account(id, data)
                return Response(token_data, status=status.HTTP_200_OK)
    except ValueError:
        return Response(token_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view (['GET','POST'])
@permission_classes([AllowAny, ])
def get_communes(request):
    try:
        service = ComunaService()
        comunas = service.get_all()
        return Response(comunas, status=status.HTTP_200_OK)
    except ValueError:
        return Response(comunas, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view (['GET','POST'])
@permission_classes([AllowAny, ])
def verify_token(request):
    try:
        token = request.META['HTTP_AUTHORIZATION']
        service = UsuarioService()
        token_data = service.decode_token(token)
        return Response(token_data,status=status.HTTP_200_OK)
    except ValueError:
        return Response(token_data,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
