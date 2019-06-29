from django.db import models



class TipoPropiedad(models.Model):
    nid_tipo_propiedad = models.AutoField(db_column='NId_tipo_propiedad', primary_key=True)  # Field name made lowercase.
    snombre_tipo_propiedad = models.CharField(db_column='SNombre_tipo_propiedad', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_tipo_propiedad = models.CharField(db_column='SDescripcion_tipo_propiedad', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nidestadoregistro_tipo_propiedad = models.IntegerField(db_column='NIdEstadoRegistro_tipo_propiedad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_propiedad'