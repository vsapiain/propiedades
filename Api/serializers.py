#from PropiedadesApp.models.usuario_model import Usuario
from PropiedadesApp.models import Usuario

from PropiedadesApp.proxy.usuario_proxy import  usuario_proxy
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email','clave')
