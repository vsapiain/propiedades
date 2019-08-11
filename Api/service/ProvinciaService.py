from Api.models import Provincia
from Api.serializers import ProvinciaSerializer
#from django.core import serializers

class ProvinciaService:
    def get_all(self):
        comuna_data = {}
        msg = ""
        error = 0
        try:
            data =  Provincia.objects.order_by('snombre_provincia')
            data_serializer = ProvinciaSerializer(data,many=True)
        except Provincia.DoesNotExist:
            comuna_data["error"] = 1
            comuna_data["msg"] = "Comunas inexistentes"
            comuna_data["data"] = ""
            return comuna_data
        except Exception as err:
            msg = err
            error = 1
            data = ""
        finally:
            comuna_data["msg"] = msg
            comuna_data["error"] = error
            comuna_data["data"] = data_serializer.data
            return comuna_data
