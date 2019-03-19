from django.db import models


class Direccion(models.Model):
    nid_direccion = models.AutoField(db_column='NId_Direccion', primary_key=True)  # Field name made lowercase.
    nid_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='NId_Comuna', blank=True, null=True)  # Field name made lowercase.
    sdireccion_direccion = models.CharField(db_column='SDireccion_Direccion', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    slatitud_direccion = models.CharField(db_column='SLatitud_Direccion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    slongitud_direccion = models.CharField(db_column='SLongitud_Direccion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nidreferencia_direccion = models.IntegerField(db_column='NIdReferencia_Direccion', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_direccion = models.IntegerField(db_column='NEstadoRegistro_Direccion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'direccion'
