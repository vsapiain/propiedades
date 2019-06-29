from django.db import models


class DetalleNotaVenta(models.Model):
    nid_detalle_nota_venta = models.AutoField(db_column='NId_detalle_nota_venta', primary_key=True)  # Field name made lowercase.
    nid_nota_venta = models.ForeignKey('NotaVenta', models.DO_NOTHING, db_column='NId_nota_venta', blank=True, null=True)  # Field name made lowercase.
    ncantidad_nota_venta = models.IntegerField(db_column='NCantidad_nota_venta', blank=True, null=True)  # Field name made lowercase.
    nprecio_nota_venta = models.IntegerField(db_column='NPrecio_nota_venta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_nota_venta'