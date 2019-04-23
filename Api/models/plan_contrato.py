from django.db import models


class PlanContrato(models.Model):
    nid_plan_contrato = models.AutoField(db_column='NId_plan_contrato', primary_key=True)  # Field name made lowercase.
    snombre_plan_contrato = models.CharField(db_column='SNombre_plan_contrato', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdetalle_plan_contrato = models.CharField(db_column='SDetalle_plan_contrato', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ffechainiciovigencia_plan_contrato = models.DateTimeField(db_column='FFechaInicioVigencia_plan_contrato', blank=True, null=True)  # Field name made lowercase.
    ffechafinvigencia_plan_contrato = models.DateTimeField(db_column='FFechaFinVigencia_plan_contrato', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_plan_contrato = models.IntegerField(db_column='NEstadoRegistro_plan_contrato', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plan_contrato'
