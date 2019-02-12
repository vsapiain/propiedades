from django.db import models


class LineaFactura(models.Model):
    nid_linea_factura = models.AutoField(db_column='NId_linea_factura', primary_key=True)  # Field name made lowercase.
    ncantidad_factura = models.IntegerField(db_column='NCantidad_factura', blank=True, null=True)  # Field name made lowercase.
    nprecio_factura = models.IntegerField(db_column='NPrecio_factura', blank=True, null=True)  # Field name made lowercase.
    sdescripcion_factura = models.CharField(db_column='SDescripcion_factura', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    ddescuento_factura = models.DecimalField(db_column='DDescuento_factura', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nid_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='NId_factura', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_factura = models.IntegerField(db_column='NEstadoRegistro_factura', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'linea_factura'
