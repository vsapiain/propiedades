from Api.models import Comuna
from django.core import serializers

class ComunaService:
    def get_all(self):
        data =  Comuna.objects.order_by('snombre_comuna')
        comuna_data = {}
        comuna_data["error"] = "0"
        comuna_data["msg"] = ""
        comuna_data["obj"] = ""
        if len(list(data))<1:
            comuna_data["error"]="1"
            comuna_data["msg"] = "No existen comunas"
        else:
            comuna_data["obj"] = serializers.serialize('json', data)
        return comuna_data
