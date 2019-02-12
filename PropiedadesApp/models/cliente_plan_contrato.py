from django.db import models


class ClientePlanContrato(models.Model):
    nid_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='NId_cliente', primary_key=True)  # Field name made lowercase.
    nid_plan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='NId_plan')  # Field name made lowercase.
    ffechavigenciainicio_cliente_plan = models.DateTimeField(db_column='FFechaVigenciaInicio_cliente_plan', blank=True, null=True)  # Field name made lowercase.
    ffechavigenciatermino_cliente_plan = models.DateTimeField(db_column='FFechaVigenciaTermino_cliente_plan', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_cliente_plan = models.IntegerField(db_column='NEstadoRegistro_cliente_plan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente_plan_contrato'
        unique_together = (('nid_cliente', 'nid_plan'),)
