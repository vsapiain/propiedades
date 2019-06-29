from django.db import models


class TipoServicio(models.Model):
    nid_tipo_servicio = models.AutoField(db_column='NId_tipo_servicio', primary_key=True)  # Field name made lowercase.
    snombre_tipo_servicio = models.CharField(db_column='SNombre_tipo_servicio', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_tipo_servicio = models.CharField(db_column='SDescripcion_tipo_servicio', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_tipo_servicio = models.IntegerField(db_column='NEstadoRegistro_tipo_servicio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_servicio'