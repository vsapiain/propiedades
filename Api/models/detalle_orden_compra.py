from django.db import models


class DetalleOrdenCompra(models.Model):
    nid_detalle_orden_compra = models.AutoField(db_column='NId_detalle_orden_compra', primary_key=True)  # Field name made lowercase.
    ncantidad_detalle_orden_compra = models.IntegerField(db_column='NCantidad_detalle_orden_compra', blank=True, null=True)  # Field name made lowercase.
    nprecio_detalle_orden_compra = models.IntegerField(db_column='NPrecio_detalle_orden_compra', blank=True, null=True)  # Field name made lowercase.
    sdescripcion_detalle_orden_compra = models.CharField(db_column='SDescripcion_detalle_orden_compra', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    ddescuento_detalle_orden_compra = models.DecimalField(db_column='DDescuento_detalle_orden_compra', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    field_nid_orden_compra = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='_NId_orden_compra', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    nestadoregistro_detalle_orden_compra = models.IntegerField(db_column='NEstadoRegistro_detalle_orden_compra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_orden_compra'
