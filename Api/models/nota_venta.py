from django.db import models


class NotaVenta(models.Model):
    nid_nota_venta = models.AutoField(db_column='NId_nota_venta', primary_key=True)  # Field name made lowercase.
    nid_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='NId_factura', blank=True, null=True)  # Field name made lowercase.
    nid_estado_nota_venta = models.ForeignKey('EstadoNotaVenta', models.DO_NOTHING, db_column='NId_estado_nota_venta', blank=True, null=True)  # Field name made lowercase.
    nid_documento = models.ForeignKey('Documento', models.DO_NOTHING, db_column='NId_documento', blank=True, null=True)  # Field name made lowercase.
    ffechacreacion_nota_venta = models.DateTimeField(db_column='FFechaCreacion_nota_venta', blank=True, null=True)  # Field name made lowercase.
    ffechaemision_nota_venta = models.DateTimeField(db_column='FFechaEmision_nota_venta', blank=True, null=True)  # Field name made lowercase.
    sobservacion_nota_venta = models.CharField(db_column='SObservacion_nota_venta', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    ntotalneto_nota_venta = models.IntegerField(db_column='NTotalNeto_nota_venta', blank=True, null=True)  # Field name made lowercase.
    ncantidad_nota_venta = models.IntegerField(db_column='NCantidad_nota_venta', blank=True, null=True)  # Field name made lowercase.
    ntotalbruto_nota_venta = models.IntegerField(db_column='NTotalBruto_nota_venta', blank=True, null=True)  # Field name made lowercase.
    diva_nota_venta = models.DecimalField(db_column='DIVA_nota_venta', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_nota_venta = models.IntegerField(db_column='NEstadoRegistro_nota_venta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nota_venta'
