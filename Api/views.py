from rest_framework import permissions,status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
#from rest_framework.views import APIView
from Api.service import UsuarioService
#from PropiedadesApp.proxy import  cuenta_acceso_proxy
#from .serializers import UsuarioSerializer
#from rest_framework_jwt.settings import api_settings
#import jwt,json

@api_view (['GET'])
def user_list(request):
    pass

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


