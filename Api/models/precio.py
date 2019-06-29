from django.db import models


class Precio(models.Model):
    nid_precio = models.AutoField(db_column='NId_precio', primary_key=True)  # Field name made lowercase.
    nid_valor_precio = models.IntegerField(db_column='NId_valor_precio', blank=True, null=True)  # Field name made lowercase.
    nvigenciainicial_precio = models.DateTimeField(db_column='NVigenciaInicial_precio', blank=True, null=True)  # Field name made lowercase.
    nvigenciafinal_precio = models.DateTimeField(db_column='NVigenciaFinal_precio', blank=True, null=True)  # Field name made lowercase.
    nid_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='NId_servicio', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_precio = models.IntegerField(db_column='NEstadoRegistro_precio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'precio'
