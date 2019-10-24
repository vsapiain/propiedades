from Api.models import Direccion
from Api.models import Comuna
from Api.models import Propiedad
from Api.models import TipoPropiedad
from django.db import transaction
from django.db import IntegrityError
from datetime import datetime
from rest_framework import status

class PropiedadService():
    def get_all(self):
        return Propiedad.objects.all()

    def save(self,scodigo,ntipo_propiedad,sdireccion,ncomuna,ntotal_habitacion,ntotal_bannos,
             ntotal_estacionamientos,dmts2_contruidos,dmt2_total,naire_acondicionado,nparrilla,nsecadora,ngimnasio,
             nlavanderia,ncesped,nmicroonda,nducha,nrefrigerador,nsauna,npiscina,ntvcable,nlavadora,nwifi,nbodega,
             ffecha_vigencia_inicial,ffecha_vigencia_final,nestado_registro):
        finicial = datetime.now() if ffecha_vigencia_inicial is None else str(ffecha_vigencia_inicial)
        comuna_instance = Comuna.objects.get(nid_comuna=ncomuna)
        tipo_propiedad_instance = TipoPropiedad.objects.get(nid_tipo_propiedad=ntipo_propiedad)
        msg = ''
        error = 0
        status_err = ''
        data = ''
        resp = {}
        try:
            with transaction.atomic():
                direccion_instance = Direccion.objects.create(nid_comuna=comuna_instance,sdireccion_direccion = sdireccion,nestadoregistro_direccion=1)
                propiedad_instance =  Propiedad.objects.create(scodigo_propiedad=scodigo,nid_tipo_propiedad=tipo_propiedad_instance,
                                                nid_direccion=direccion_instance,
                                                ntotal_habitacion_propiedad=ntotal_habitacion,
                                                ntotal_bannos_propiedad=ntotal_bannos,
                                                ntotal_estacionamiento_propiedad=ntotal_estacionamientos,
                                                nmts2_construido_propiedad=dmts2_contruidos,nmts2_total_propiedad=dmt2_total,
                                                naireacondicionado_propiedad=naire_acondicionado,nparrilla_propiedad=nparrilla,
                                                nsecadora_propiedad=nsecadora,ngimnasio_propiedad=ngimnasio,
                                                nlavanderia_propiedad=nlavanderia,ncesped_propiedad=ncesped,
                                                nmicroonda_propiedad=nmicroonda,nducha_propiedad=nducha,
                                                nrefrigerador_propiedad=nrefrigerador,nsauna_propiedad=nsauna,
                                                npiscina_propiedad=npiscina,ntvcable_propiedad=ntvcable,
                                                nlavadora_propiedad=nlavadora,nwifi_propiedad=nwifi,nbodega_propiedad=nbodega,
                                                ffechavigenciainicial_propiedad=finicial,
                                                fvigenciafinal_propiedad=ffecha_vigencia_final,
                                                nestadoregistro_propiedad=nestado_registro)

                data =  propiedad_instance
                status_err = status.HTTP_200_OK
        except IntegrityError:
            status_err = status.HTTP_500_INTERNAL_SERVER_ERROR
            error = 1
            msg = 'Error registro propiedad'
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