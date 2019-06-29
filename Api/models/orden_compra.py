from django.db import models


class OrdenCompra(models.Model):
    field_nid_orden_compra = models.AutoField(db_column='_NId_orden_compra', primary_key=True)  # Field name made lowercase. Field renamed because it started with '_'.
    nnumero_orden_compra = models.IntegerField(db_column='NNumero_orden_compra', blank=True, null=True)  # Field name made lowercase.
    ffechacreacion_orden_compra = models.DateTimeField(db_column='FFechaCreacion_orden_compra', blank=True, null=True)  # Field name made lowercase.
    ffechaemision_orden_compra = models.DateTimeField(db_column='FFechaEmision_orden_compra', blank=True, null=True)  # Field name made lowercase.
    sobservacion_orden_compra = models.CharField(db_column='SObservacion_orden_compra', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    ntotal_orden_compra = models.IntegerField(db_column='NTotal_orden_compra', blank=True, null=True)  # Field name made lowercase.
    ncantidadcompra_orden_compra = models.IntegerField(db_column='NCantidadCompra_orden_compra', blank=True, null=True)  # Field name made lowercase.
    ddescuentoglobal_orden_compra = models.DecimalField(db_column='DDescuentoGlobal_orden_compra', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_orden_compra = models.IntegerField(db_column='NEstadoRegistro_orden_compra', blank=True, null=True)  # Field name made lowercase.
    nid_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='NId_factura', blank=True, null=True)  # Field name made lowercase.
    nid_documento = models.ForeignKey('Documento', models.DO_NOTHING, db_column='NId_documento', blank=True, null=True)  # Field name made lowercase.
    nid_estado_orden_compra = models.ForeignKey('EstadoOrdenCompra', models.DO_NOTHING, db_column='NId_estado_orden_compra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orden_compra'
