from django.db import models


class TipoPlanContrato(models.Model):
    nid_tipo_plan_contrato = models.AutoField(db_column='NId_tipo_plan_contrato', primary_key=True)  # Field name made lowercase.
    snombre_tipo_plan_contratro = models.CharField(db_column='SNombre_tipo_plan_contratro', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_tipo_plan_contrato = models.CharField(db_column='SDescripcion_tipo_plan_contrato', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nidestadoregistro_tipo_plan_contrato = models.IntegerField(db_column='NIdEstadoRegistro_tipo_plan_contrato', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_plan_contrato'
