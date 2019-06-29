from django.db import models


class Pedido(models.Model):
    nid_pedido = models.IntegerField(db_column='NId_pedido', primary_key=True)  # Field name made lowercase.
    nid_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='NId_usuario', blank=True, null=True)  # Field name made lowercase.
    sobservacion_pedido = models.CharField(db_column='SObservacion_pedido', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_pedido = models.IntegerField(db_column='NEstadoRegistro_pedido', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedido'
