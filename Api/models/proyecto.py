from django.db import models


class Proyecto(models.Model):
    nid_proyecto = models.AutoField(db_column='NId_proyecto', primary_key=True)  # Field name made lowercase.
    nid_inmobiliaria = models.ForeignKey('Inmobiliaria', models.DO_NOTHING, db_column='NId_inmobiliaria', blank=True, null=True)  # Field name made lowercase.
    nnombre_proyecto = models.CharField(db_column='NNombre_proyecto', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_proyecto = models.IntegerField(db_column='NEstadoRegistro_proyecto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proyecto'