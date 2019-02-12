from django.db import models


class EstadoPropiedad(models.Model):
    nid_estado_propiedad = models.AutoField(db_column='NId_estado_propiedad', primary_key=True)  # Field name made lowercase.
    snombre_estado_propiedad = models.CharField(db_column='SNombre_estado_propiedad', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sdetalle_estado_propiedad = models.CharField(db_column='SDetalle_estado_propiedad', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_estado_propiedad = models.IntegerField(db_column='NEstadoRegistro_estado_propiedad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado_propiedad'
