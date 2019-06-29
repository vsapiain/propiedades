from django.db import models


class EstadoNotaVenta(models.Model):
    nid_estado_nota_venta = models.AutoField(db_column='NId_estado_nota_venta', primary_key=True)  # Field name made lowercase.
    snombre_estado_nota_venta = models.CharField(db_column='SNombre_estado_nota_venta', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_estado_nota_venta = models.CharField(db_column='SDescripcion_estado_nota_venta', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_estado_nota_venta = models.IntegerField(db_column='NEstadoRegistro_estado_nota_venta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado_nota_venta'
