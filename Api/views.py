from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from PropiedadesApp.models import Usuario
from Api.service import usuario_service
from .serializers import UsuarioSerializer

@api_view (['GET'])
def user_list(request):
    if request.method == 'GET':
        service = usuario_service()
        usuarios = service.list_users()
        serializer = UsuarioSerializer(usuarios, many=True)
        #obj_usuario = usuario_prox.get_by_email('admin@gmail.com')
    return Response(serializer.data)