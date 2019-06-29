from django.db import models


class DocumentoPedido(models.Model):
    nid_documento_pedido = models.AutoField(db_column='NId_documento_pedido', primary_key=True)  # Field name made lowercase.
    nid_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='NId_pedido')  # Field name made lowercase.
    nid_documento = models.ForeignKey('Documento', models.DO_NOTHING, db_column='NId_documento')  # Field name made lowercase.
    nestado_documento_pedido = models.IntegerField(db_column='NEstado_documento_pedido', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'documento_pedido'
