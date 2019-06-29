from django.db import models


class ServicioPedido(models.Model):
    nid_servicio_pedido = models.AutoField(db_column='NId_servicio_pedido', primary_key=True)  # Field name made lowercase.
    nid_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='NId_servicio')  # Field name made lowercase.
    nid_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='NId_pedido')  # Field name made lowercase.
    nestadoregistro_pedido = models.IntegerField(db_column='NEstadoRegistro_pedido', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicio_pedido'
