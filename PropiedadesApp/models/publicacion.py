from django.db import models


class Publicacion(models.Model):
    nid_publicacion = models.AutoField(db_column='NId_publicacion', primary_key=True)  # Field name made lowercase.
    nid_plan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='NId_plan', blank=True, null=True)  # Field name made lowercase.
    sdescripcion_publicacion = models.CharField(db_column='SDescripcion_publicacion', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    ffechainiciovigencia_publicacion = models.DateTimeField(db_column='FFechaInicioVigencia_publicacion', blank=True, null=True)  # Field name made lowercase.
    ffechafinvigencia_publicacion = models.DateTimeField(db_column='FFechaFinVigencia_publicacion', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_publicacion = models.IntegerField(db_column='NEstadoRegistro_publicacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publicacion'
