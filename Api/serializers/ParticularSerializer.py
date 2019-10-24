from rest_framework import serializers
from  Api.models import particular

class ParticularSerializer(serializers.ModelSerializer):

    class Meta:
        model = particular
        fields = '__all__'
