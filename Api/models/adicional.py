from django.db import models


class Adicional(models.Model):
    nid_adicional = models.AutoField(db_column='NId_adicional', primary_key=True)  # Field name made lowercase.
    nid_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='NId_servicio', blank=True, null=True)  # Field name made lowercase.
    snombre_adicional = models.CharField(db_column='SNombre_adicional', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_adicional = models.CharField(db_column='SDescripcion_adicional', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_adicional = models.IntegerField(db_column='NEstadoRegistro_adicional', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adicional'
