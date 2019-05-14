#from PropiedadesApp.models.usuario_model import Usuario
from PropiedadesApp.models import CuentaAcceso

from PropiedadesApp.proxy.UsuarioProxy import  UsuarioProxy
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaAcceso
        fields = ('SEmail_cuenta_acceso','SClave_cuenta_acceso')
