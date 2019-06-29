from django.db import models



class PropiedadProyecto(models.Model):
    nid_propiedad_proyecto = models.AutoField(db_column='NId_propiedad_proyecto', primary_key=True)  # Field name made lowercase.
    nid_propiedad = models.ForeignKey('Propiedad', models.DO_NOTHING, db_column='NId_propiedad')  # Field name made lowercase.
    nid_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='NId_proyecto')  # Field name made lowercase.
    nidestadoregistro_propiedad_proyecto = models.IntegerField(db_column='NIdEstadoRegistro_propiedad_proyecto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propiedad_proyecto'