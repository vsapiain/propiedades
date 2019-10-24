from Api.models import Provincia
from Api.serializers import ProvinciaSerializer
#from django.core import serializers

class ProvinciaService:
    def get_all(self):
        msg = ''
        error = 0
        status_err = ''
        data = ''
        resp = {}
        try:
            data =  Provincia.objects.order_by('snombre_provincia')
            data_serializer = ProvinciaSerializer(data,many=True)
        except Provincia.DoesNotExist:
            resp["error"] = 1
            resp["msg"] = "Comunas inexistentes"
            resp["data"] = ""
            return resp
        except Exception as err:
            msg = err
            error = 1
            data = ""
        finally:
            resp["msg"] = msg
            resp["error"] = error
            resp["data"] = data_serializer.data
            return resp
