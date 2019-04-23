from django.db import models


class UsuarioPlanContrato(models.Model):
    nid_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='NId_usuario', primary_key=True)  # Field name made lowercase.
    nid_plan_contrato = models.ForeignKey('PlanContrato', models.DO_NOTHING, db_column='NId_plan_contrato')  # Field name made lowercase.
    ffechavigenciainicio_cliente_plan = models.DateTimeField(db_column='FFechaVigenciaInicio_cliente_plan', blank=True, null=True)  # Field name made lowercase.
    ffechavigenciatermino_cliente_plan = models.DateTimeField(db_column='FFechaVigenciaTermino_cliente_plan', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_cliente_plan = models.IntegerField(db_column='NEstadoRegistro_cliente_plan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_plan_contrato'
        unique_together = (('nid_usuario', 'nid_plan_contrato'),)
