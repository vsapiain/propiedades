from django.db import models


class EstadoFactura(models.Model):
    nid_estado_factura = models.AutoField(db_column='NId_estado_factura', primary_key=True)  # Field name made lowercase.
    snombre_estado_factura = models.CharField(db_column='SNombre_estado_factura', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_estado_factura = models.CharField(db_column='SDescripcion_estado_factura', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nestradoregistro_estado_factura = models.IntegerField(db_column='NEstradoRegistro_estado_factura', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado_factura'
