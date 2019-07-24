from Api.models import Publicacion
from Api.models import CuentaAcceso
from Api.models import Propiedad
from Api.models import PlanContrato
from Api.models import Operacion
from django.db import transaction
from django.db import IntegrityError
from datetime import datetime

class PublicacionService():
    def get_all(self):
        return Publicacion.objects.all()

    def save(self,npropiedad,nplan,ncuenta,noperacion,stitulo,sdescripcion,finicio_vigencia,ffinal_vigencia,sobservacion,nestado):
        usuario_instance = CuentaAcceso.objects.get(nid_cuenta_acceso=ncuenta).nid_usuario
        propiedad_instance = Propiedad.objects.filter(nid_propiedad=npropiedad).get()
        operacion_instance =  Operacion.objects.filter(nid_operacion=noperacion).get()
        plan_instance = PlanContrato.objects.filter(nid_plan_contrato=nplan).get()
        finicial = datetime.now() if finicio_vigencia is None else str(finicio_vigencia)
        #ffinal = time.strftime("%c") if ffinal_vigencia is None else str(ffinal_vigencia)
        try:
            with transaction.atomic():
                publicacion_instance = Publicacion.objects.create(nid_propiedad=propiedad_instance,nid_plan_contrato=plan_instance,
                                           nid_usuario=usuario_instance,nid_operacion=operacion_instance,stitulo_publicacion=stitulo,
                                           sdescripcion_publicacion=sdescripcion,ffechacreacion_publicacion=datetime.now(),
                                           ffechainiciovigencia_publicacion=finicial,ffechafinvigencia_publicacion=ffinal_vigencia,
                                           sobservacion_publicacion=sobservacion,nestadoregistro_publicacion=nestado)
                return publicacion_instance
        except IntegrityError:
            return None

