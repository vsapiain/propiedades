from rest_framework import serializers
from  Api.models import Comuna

class ComunaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comuna
        fields = '__all__'
