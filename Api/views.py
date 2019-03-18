from rest_framework import permissions,status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from Api.service import usuario_service
from PropiedadesApp.proxy import  cuenta_acceso_proxy
#from .serializers import UsuarioSerializer
from rest_framework_jwt.settings import api_settings
import jwt,json

'''
@api_view (['GET'])
def user_list(request):
    if request.method == 'GET':
        service = usuario_service()
        usuarios = service.list_users()
        serializer = UsuarioSerializer(usuarios, many=True)
        #obj_usuario = usuario_prox.get_by_email('admin@gmail.com')
    return Response(serializer.data)
'''
@api_view (['GET'])
def user_list(request):
    pass

@api_view (['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    if request.method == 'POST':
        service = usuario_service()
        tipo_usuario = request.data['tipo']
        password = request.data['password']
        usuario = request.data['usuario']
        if tipo_usuario == "1":
            data = service.is_authenticated_particular(usuario,password)
            if data["token"]!="":
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        else:
            if tipo_usuario == 2:
                #cliente_empresa = service.get_user_corredora(password, usuario)
                pass
            else:
                #cliente_empresa = service.get_user_inmobiliaria(password, usuario)
                pass


@api_view (['GET'])
@permission_classes([AllowAny, ])
def verify_token(request):
    try:
        if request.method == 'GET':
            token = request.META['HTTP_AUTHORIZATION']
            service = usuario_service()
            token_data = service.decode_token(token)
            return Response(token_data)


    except ValueError:
        pass


