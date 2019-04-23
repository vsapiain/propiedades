from django.db import models


class Operacion(models.Model):
    nid_operacion = models.AutoField(db_column='NId_operacion', primary_key=True)  # Field name made lowercase.
    nid_tipo_operacion = models.ForeignKey('TipoOperacion', models.DO_NOTHING, db_column='NId_tipo_operacion', blank=True, null=True)  # Field name made lowercase.
    ffechacreacion_operacion = models.DateTimeField(db_column='FFechaCreacion_operacion', blank=True, null=True)  # Field name made lowercase.
    nid_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='NId_usuario', blank=True, null=True)  # Field name made lowercase.
    nidestadoregistro_operacion = models.IntegerField(db_column='NIdEstadoRegistro_operacion', blank=True, null=True)  # Field name made lowercase.
    sobservacion_operacion = models.CharField(db_column='SObservacion_operacion', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'operacion'
