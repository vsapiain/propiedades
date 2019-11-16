from Api.models import Fotografia
from django.db import transaction
from django.db import IntegrityError
from rest_framework import status

class FotografiaService:
    def save(self,publicacion,codigo,nombre,path,peso):
        msg = ''
        error = 0
        status_err = ''
        data = ''
        resp = {}
        try:
            with transaction.atomic():
                #Fotografia.object.create()
                #data =  propiedad_instance
                status_err = status.HTTP_200_OK
        except IntegrityError:
            status_err = status.HTTP_500_INTERNAL_SERVER_ERROR
            error = 1
            msg = 'Error subir al imagen'
        except Exception as err:
            msg = str(err)
            status_err = status.HTTP_500_INTERNAL_SERVER_ERROR
            error = 1
        finally:
            resp["msg"] = msg
            resp["error"] = error
            resp["data"] = data
            resp["error"] = error
            resp["status"] = status_err
        return resp