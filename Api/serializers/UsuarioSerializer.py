from rest_framework import serializers
from  Api.models import usuario

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = usuario
        fields = '__all__'
