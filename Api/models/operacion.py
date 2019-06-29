from django.db import models


class Operacion(models.Model):
    nid_operacion = models.AutoField(db_column='NId_operacion', primary_key=True)  # Field name made lowercase.
    snombre_operacion = models.CharField(db_column='SNombre_operacion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_operacion = models.CharField(db_column='SDescripcion_operacion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nidestadoregistro_operacion = models.IntegerField(db_column='NIdEstadoRegistro_operacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'operacion'