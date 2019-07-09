from Api.models import Propiedad
from Api.models import Direccion
from django.core import serializers
class PropiedadService():

    def get_all(self):
        data =  Propiedad.objects.all()
        return data

    def save(self,scodigo,ntipo_propiedad,sdireccion,ncomuna,ntotal_habitacion,ntotal_bannos,ntotal_estacionamientos,dmts2_contruidos,
             dmt2_total,naire_acondicionado,nparrilla,nsecadora,ngimnasio,nlavanderia,ncesped,nmicroonda,nducha,nrefrigerador,
             nsauna,npiscina,ntvcable,nlavadora,nwifi,ffecha_vigencia_inicial,ffecha_vigencia_final,nestado_registro):
        direccion_obj = Direccion(nid_comuna =ncomuna,sdireccion_direccion = sdireccion,nestadoregistro_direccion=1)
        direccion_obj.save()
        id_direccion = direccion_obj.nid_direccion
        direccion_obj.commit()