from django.db import models


class DetalleFactura(models.Model):
    nid_detalle_factura = models.AutoField(db_column='NId_detalle_factura', primary_key=True)  # Field name made lowercase.
    ncantidad_detalle_factura = models.IntegerField(db_column='NCantidad_detalle_factura', blank=True, null=True)  # Field name made lowercase.
    nprecio_detalle_factura = models.IntegerField(db_column='NPrecio_detalle_factura', blank=True, null=True)  # Field name made lowercase.
    sdescripcion_detalle_factura = models.CharField(db_column='SDescripcion_detalle_factura', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    ddescuento_detalle_factura = models.DecimalField(db_column='DDescuento_detalle_factura', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_detalle_factura = models.IntegerField(db_column='NEstadoRegistro_detalle_factura', blank=True, null=True)  # Field name made lowercase.
    nid_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='NId_factura', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_factura'
