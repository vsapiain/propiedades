from django.db import models


class Fotografia(models.Model):
    nid_fotografia = models.AutoField(db_column='NId_fotografia', primary_key=True)  # Field name made lowercase.
    nid_publicacion = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='NId_publicacion', blank=True, null=True)  # Field name made lowercase.
    sui_fotografia = models.CharField(db_column='SUI_fotografia', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    snombre_fotografia = models.CharField(db_column='SNombre_fotografia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    snombrecompleto_fotografia = models.CharField(db_column='SNombreCompleto_fotografia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sextension_fotografia = models.CharField(db_column='SExtension_fotografia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_fotografia = models.IntegerField(db_column='NEstadoRegistro_fotografia', blank=True, null=True)  # Field name made lowercase.
    ntamano_fotografia = models.IntegerField(db_column='NTamano_fotografia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fotografia'
