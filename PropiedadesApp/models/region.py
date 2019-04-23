from django.db import models


class Region(models.Model):
    nid_region = models.AutoField(db_column='NId_Region', primary_key=True)  # Field name made lowercase.
    snombre_region = models.CharField(db_column='SNombre_Region', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nidreferencia_region = models.IntegerField(db_column='NIdReferencia_Region', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_region = models.IntegerField(db_column='NEstadoRegistro_Region', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'
