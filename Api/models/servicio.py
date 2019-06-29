from django.db import models


class Servicio(models.Model):
    nid_servicio = models.AutoField(db_column='NId_servicio', primary_key=True)  # Field name made lowercase.
    nid_tipo_servicio = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='NId_tipo_servicio', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_servicio = models.IntegerField(db_column='NEstadoRegistro_servicio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicio'

