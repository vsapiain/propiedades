from django.db import models


class Comuna(models.Model):
    nid_comuna = models.AutoField(db_column='NId_Comuna', primary_key=True)  # Field name made lowercase.
    nid_provincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='NId_Provincia', blank=True, null=True)  # Field name made lowercase.
    snombre_comuna = models.CharField(db_column='SNombre_Comuna', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nidreferencia_comuna = models.IntegerField(db_column='NIdReferencia_Comuna', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_comuna = models.IntegerField(db_column='NEstadoRegistro_Comuna', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comuna'
