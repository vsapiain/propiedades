from django.db import models


class Plan(models.Model):
    nid_plan = models.AutoField(db_column='NId_plan', primary_key=True)  # Field name made lowercase.
    snombre_plan = models.CharField(db_column='SNombre_plan', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdetalle_plan = models.CharField(db_column='SDetalle_plan', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ffechainiciovigencia_plan = models.DateTimeField(db_column='FFechaInicioVigencia_plan', blank=True, null=True)  # Field name made lowercase.
    ffechafinvigencia_plan = models.DateTimeField(db_column='FFechaFinVigencia_plan', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_plan = models.IntegerField(db_column='NEstadoRegistro_plan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plan'
