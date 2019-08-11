from rest_framework import serializers
from  Api.models import Provincia
#from Api.serializers.ComunaSerializer import ComunaSerializer

class ProvinciaSerializer(serializers.ModelSerializer):
    #comunas = ComunaSerializer(many=True, read_only=True)
    class Meta:
        model = Provincia
        fields = '__all__'
        #fields = ['snombre_provincia','comunas']
