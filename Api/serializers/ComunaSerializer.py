from rest_framework import serializers
#from Api.serializers.ProvinciaSerializer import ProvinciaSerializer
from  Api.models import Comuna
from  Api.models import Provincia

class ComunaSerializer(serializers.ModelSerializer):
    #provincias = ProvinciaSerializer(many=True, read_only=True)
    class Meta:
        model = Comuna
        fields = '__all__'
        #depth = 1
        #fields = ['nid_comuna','snombre_comuna']
