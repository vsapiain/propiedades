from django.db import models


class EstadoOrdenCompra(models.Model):
    nid_estado_orden_compra = models.AutoField(db_column='NId_estado_orden_compra', primary_key=True)  # Field name made lowercase.
    snombre_estado_orden_compra = models.CharField(db_column='SNombre_estado_orden_compra', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_estado_orden_compra = models.CharField(db_column='SDescripcion_estado_orden_compra', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_estado_orden_compra = models.IntegerField(db_column='NEstadoRegistro_estado_orden_compra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado_orden_compra'
