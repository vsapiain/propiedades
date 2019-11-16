from Api.models import Publicacion
from Api.models import CuentaAcceso
from Api.models import Propiedad
from Api.models import PlanContrato
from Api.models import Operacion
from Api.serializers import PublicacionSerializer
from django.db import transaction
from django.db import IntegrityError
from datetime import datetime
from rest_framework import status

class PublicacionService():
    def get_all(self):
        resp = {}
        msg = ""
        error = 0
        status_err = ''
        data = ''
        try:
            estado_activo = 1
            resp_data = Publicacion.objects.filter(nestadoregistro_publicacion=estado_activo).all()
            data = PublicacionSerializer(resp_data,many=True).data
            status_err = status.HTTP_200_OK
        except IntegrityError as e:
            status_err = status.HTTP_500_INTERNAL_SERVER_ERROR
            error = 1
            msg = 'Error registro publicación'
        finally:
            resp["msg"] = msg
            resp["error"] = error
            resp["data"] = data
            resp["status"] = status_err
            return resp




    def save(self,npropiedad,nplan,ncuenta,noperacion,stitulo,sdescripcion,finicio_vigencia,ffinal_vigencia,sobservacion,
             tipo_cambio,gastos_comunes,precio,nestado):
        tipo_peso  = 1
        tipo_uf = 2
        msg = ''
        error = 0
        status_err = ''
        data = ''
        resp = {}
        if int(tipo_cambio) == tipo_peso:
            precio_peso = precio
            precio_uf = -1
        else:
            precio_uf = float(precio)
            precio_peso = -1
        usuario_instance = CuentaAcceso.objects.get(nid_cuenta_acceso=ncuenta).nid_usuario
        propiedad_instance = Propiedad.objects.filter(nid_propiedad=npropiedad).get()
        operacion_instance =  Operacion.objects.filter(nid_operacion=noperacion).get()
        plan_instance = PlanContrato.objects.filter(nid_plan_contrato=nplan).get()
        finicial = datetime.now() if finicio_vigencia is None else str(finicio_vigencia)
        try:
            with transaction.atomic():
                publicacion_instance = Publicacion.objects.create(nid_propiedad=propiedad_instance,nid_plan_contrato=plan_instance,
                                            nid_usuario=usuario_instance,nid_operacion=operacion_instance,stitulo_publicacion=stitulo,
                                            sdescripcion_publicacion=sdescripcion,ffechacreacion_publicacion=datetime.now(),
                                            ffechainiciovigencia_publicacion=finicial,ffechafinvigencia_publicacion=ffinal_vigencia,
                                            sobservacion_publicacion=sobservacion,nestadoregistro_publicacion=nestado,
                                            nprecioneto_publicacion=precio_peso,npreciouf_publicacion=precio_uf)
                data = publicacion_instance
                status_err = status.HTTP_200_OK
        except IntegrityError as e:
            status_err = status.HTTP_500_INTERNAL_SERVER_ERROR
            error = 1
            msg = 'Error registro publicación'
        finally:
            resp["msg"] = msg
            resp["error"] = error
            resp["data"] = data
            resp["status"] = status_err
            return resp


