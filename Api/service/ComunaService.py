from Api.models import Comuna
from Api.serializers import ComunaSerializer
#from django.core import serializers

class ComunaService:
    def get_all(self):
        comuna_data = {}
        msg = ""
        error = 0
        try:
            data =  Comuna.objects.order_by('snombre_comuna')
        except Comuna.DoesNotExist:
            comuna_data["error"] = 1
            comuna_data["msg"] = "Comunas inexistentes"
            comuna_data["data"] = ""
            return comuna_data
        try:
            data_serializer = ComunaSerializer(data,many=True)
        except Exception as err:
            msg = "Error carga Comunas"
            error = 1
            data = ""
        finally:
            comuna_data["msg"] = msg
            comuna_data["error"] = error
            comuna_data["data"] = data_serializer.data
            return comuna_data
