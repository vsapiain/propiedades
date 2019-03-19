from django.db import models


class TipoOperacion(models.Model):
    nid_tipo_operacion = models.AutoField(db_column='NId_tipo_operacion', primary_key=True)  # Field name made lowercase.
    snombre_tipo_operacion = models.CharField(db_column='SNombre_tipo_operacion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdetalle_tipo_operacion = models.CharField(db_column='SDetalle_tipo_operacion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_tipo_operacion = models.IntegerField(db_column='NEstadoRegistro_tipo_operacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_operacion'
