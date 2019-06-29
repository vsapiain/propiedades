from django.db import models


class TipoUsuario(models.Model):
    nid_tipo_usuario = models.AutoField(db_column='NId_tipo_usuario', primary_key=True)  # Field name made lowercase.
    snombre_tipo_cliente = models.CharField(db_column='SNombre_tipo_cliente', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_tipo_cliente = models.CharField(db_column='SDescripcion_tipo_cliente', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nidestadoregistro_tipo_cliente = models.IntegerField(db_column='NIdEstadoRegistro_tipo_cliente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_usuario'
