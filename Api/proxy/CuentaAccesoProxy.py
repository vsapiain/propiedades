from Api.models import CuentaAcceso
from django.db import models

class CuentaParticular(models.Manager):
    def get_queryset(self):
        tipo_particular = 1
        return super(CuentaParticular,self).get_queryset().filter(nid_usuario__nid_tipo_usuario=tipo_particular)

class CuentaCorredora(models.Manager):
    def get_queryset(self):
        tipo_corredora = 2
        return super(CuentaCorredora,self).get_queryset().filter(nid_usuario__nid_tipo_usuario=tipo_corredora)

class CuentaInmobiliaria(models.Manager):
    def get_queryset(self):
        tipo_inmobiliaria = 3
        return super(CuentaInmobiliaria,self).get_queryset().filter(nid_usuario__nid_tipo_usuario=tipo_inmobiliaria)

class CuentaAccesoProxy(CuentaAcceso):
    authenticated = False
    objects_particular = CuentaParticular()
    objects_corredora = CuentaCorredora()
    objects_inmobiliaria = CuentaInmobiliaria()
    class Meta:
        proxy = True
