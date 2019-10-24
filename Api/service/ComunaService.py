from Api.models import Comuna
from Api.serializers import ComunaSerializer
from rest_framework import status

class ComunaService:
    def get_all(self):
        comuna_data = {}
        msg = ""
        error = 0
        status_err = ''
        data = ''
        try:
            data_comuna =  Comuna.objects.order_by('snombre_comuna')
            data_serializer = ComunaSerializer(data_comuna,many=True)
            data = data_serializer.data
            status_err = status.HTTP_200_OK
        except Comuna.DoesNotExist:
            error = 1
            msg = "Comunas inexistentes"
            status_err = status.HTTP_404_NOT_FOUND
            data = ''
        except Exception as err:
            msg = "Error carga Comunas"
            error = 1
            status_err = status.HTTP_500_INTERNAL_SERVER_ERROR
            data = ''
        finally:
            comuna_data["msg"] = msg
            comuna_data["error"] = error
            comuna_data["data"] = data
            comuna_data["status"] = status_err
            return comuna_data