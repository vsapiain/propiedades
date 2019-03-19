from Api.models import CuentaAcceso
from django.db import models

class cuenta_acceso_manager(models.Manager):
    def get_queryset(self):
        return super(cuenta_acceso_manager, self).get_queryset()

class cuenta_acceso_proxy(CuentaAcceso):
    authenticated = False
    objects = cuenta_acceso_manager()

    class Meta:
        proxy = True
