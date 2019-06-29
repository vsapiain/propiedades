from django.db import models


class DetallePlanContrato(models.Model):
    nid_detalle_plan_contrato = models.AutoField(db_column='NId_detalle_plan_contrato', primary_key=True)  # Field name made lowercase.
    nid_plan_contrato = models.ForeignKey('PlanContrato', models.DO_NOTHING, db_column='NId_plan_contrato', blank=True, null=True)  # Field name made lowercase.
    sdescripcion_detalle_plan_contrato = models.CharField(db_column='SDescripcion__detalle_plan_contrato', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    nestadoregistro_detalle_plan_contrato = models.IntegerField(db_column='NEstadoRegistro_detalle_plan_contrato', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_plan_contrato'
