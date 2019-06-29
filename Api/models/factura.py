from django.db import models


class Factura(models.Model):
    nid_factura = models.AutoField(db_column='NId_factura', primary_key=True)  # Field name made lowercase.
    nid_estado_factura = models.ForeignKey('EstadoFactura', models.DO_NOTHING, db_column='NId_estado_factura', blank=True, null=True)  # Field name made lowercase.
    nid_documento = models.ForeignKey('Documento', models.DO_NOTHING, db_column='NId_documento', blank=True, null=True)  # Field name made lowercase.
    nnumero_factura = models.IntegerField(db_column='NNumero_factura', blank=True, null=True)  # Field name made lowercase.
    ffechacreacion_factura = models.DateTimeField(db_column='FFechaCreacion_factura', blank=True, null=True)  # Field name made lowercase.
    ffechaentrega_factura = models.DateTimeField(db_column='FFechaEntrega_factura', blank=True, null=True)  # Field name made lowercase.
    ffechaemision_factura = models.DateTimeField(db_column='FFechaEmision_factura', blank=True, null=True)  # Field name made lowercase.
    ffvencimiento_factura = models.DateTimeField(db_column='FFVencimiento_factura', blank=True, null=True)  # Field name made lowercase.
    sobservacion_factura = models.CharField(db_column='SObservacion_factura', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    ntotalneto_factura = models.IntegerField(db_column='NTotalNeto_factura', blank=True, null=True)  # Field name made lowercase.
    ncantidad_factura = models.IntegerField(db_column='NCantidad_factura', blank=True, null=True)  # Field name made lowercase.
    ntotalbruto_factura = models.IntegerField(db_column='NTotalBruto_factura', blank=True, null=True)  # Field name made lowercase.
    diva_factura = models.DecimalField(db_column='DIVA_factura', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ddescuentoglobal_factura = models.DecimalField(db_column='DDescuentoGlobal_factura', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_factura = models.IntegerField(db_column='NEstadoRegistro_factura', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factura'
