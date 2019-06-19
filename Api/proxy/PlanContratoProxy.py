from Api.models import PlanContrato
from django.db import models

class PlanParticular(models.Manager):
    def get_queryset(self):
        tipo_plan_particular = 1
        return super(PlanParticular,self).get_queryset().filter(nid_tipo_plan_contrato__nid_tipo_plan_contrato=tipo_plan_particular)

class PlanContratoProxy(PlanContrato):
    plan_actual = False
    objects_particular = PlanParticular()
    class Meta:
        proxy = True