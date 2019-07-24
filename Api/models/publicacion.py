from django.db import models


class Publicacion(models.Model):
    nid_publicacion = models.AutoField(db_column='NId_publicacion', primary_key=True)  # Field name made lowercase.
    nid_propiedad = models.ForeignKey('Propiedad', models.DO_NOTHING, db_column='NId_propiedad', blank=True, null=True)  # Field name made lowercase.
    nid_plan_contrato = models.ForeignKey('PlanContrato', models.DO_NOTHING, db_column='NId_plan_contrato', blank=True, null=True)  # Field name made lowercase.
    nid_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='NId_usuario', blank=True, null=True)  # Field name made lowercase.
    nid_operacion = models.ForeignKey('Operacion', models.DO_NOTHING, db_column='NId_operacion', blank=True, null=True)  # Field name made lowercase.
    stitulo_publicacion = models.CharField(db_column='STitulo_publicacion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_publicacion = models.CharField(db_column='SDescripcion_publicacion', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    ffechacreacion_publicacion = models.DateTimeField(db_column='FFechaCreacion_publicacion', blank=True, null=True)  # Field name made lowercase.
    ffechainiciovigencia_publicacion = models.DateTimeField(db_column='FFechaInicioVigencia_publicacion', blank=True, null=True)  # Field name made lowercase.
    ffechafinvigencia_publicacion = models.DateTimeField(db_column='FFechaFinVigencia_publicacion', blank=True, null=True)  # Field name made lowercase.
    sobservacion_publicacion = models.CharField(db_column='SObservacion_publicacion', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    nprecioneto_publicacion = models.IntegerField(db_column='NPrecioNeto_publicacion', blank=True, null=True)  # Field name made lowercase.
    npreciouf_publicacion = models.DecimalField(db_column='NPrecioUF_publicacion', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_publicacion = models.IntegerField(db_column='NEstadoRegistro_publicacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publicacion'
