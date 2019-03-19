from django.db import models


class LineaOrdenCompra(models.Model):
    nid_linea_orden_compra = models.AutoField(db_column='NId_linea_orden_compra', primary_key=True)  # Field name made lowercase.
    ncantidad_linea_orden_compra = models.IntegerField(db_column='NCantidad_linea_orden_compra', blank=True, null=True)  # Field name made lowercase.
    nprecio_linea_orden_compra = models.IntegerField(db_column='NPrecio_linea_orden_compra', blank=True, null=True)  # Field name made lowercase.
    sdescripcion_linea_orden_compra = models.CharField(db_column='SDescripcion_linea_orden_compra', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    ddescuento_linea_orden_compra = models.DecimalField(db_column='DDescuento_linea_orden_compra', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    field_nid_orden_compra = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='_NId_orden_compra', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    nestadoregistro_linea_orden_compra = models.IntegerField(db_column='NEstadoRegistro_linea_orden_compra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'linea_orden_compra'
