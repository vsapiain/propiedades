from django.db import models



class Provincia(models.Model):
    nid_provincia = models.AutoField(db_column='NId_Provincia', primary_key=True)  # Field name made lowercase.
    nestadoregistro_provincia = models.DecimalField(db_column='NEstadoRegistro_Provincia', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    nid_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='NId_region', blank=True, null=True)  # Field name made lowercase.
    nidreferencia_provincia = models.IntegerField(db_column='NIdReferencia_Provincia', blank=True, null=True)  # Field name made lowercase.
    snombre_provincia = models.CharField(db_column='SNombre_provincia', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provincia'