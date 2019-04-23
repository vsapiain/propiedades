from django.db import models


class Usuario(models.Model):
    nid_usuario = models.AutoField(db_column='NId_usuario', primary_key=True)  # Field name made lowercase.
    nid_tipo_usuario = models.ForeignKey('TipoUsuario', models.DO_NOTHING, db_column='NId_tipo_usuario', blank=True, null=True)  # Field name made lowercase.
    nid_direccion = models.ForeignKey('Direccion', models.DO_NOTHING, db_column='NId_Direccion', blank=True, null=True)  # Field name made lowercase.
    nrut_usuario = models.IntegerField(db_column='NRut_usuario', blank=True, null=True)  # Field name made lowercase.
    srutdigito_usuario = models.CharField(db_column='SRutDigito_usuario', max_length=10, blank=True, null=True)  # Field name made lowercase.
    srut_usuario = models.CharField(db_column='SRut_usuario', max_length=10, blank=True, null=True)  # Field name made lowercase.
    semailcontacto_usuario = models.CharField(db_column='SEmailContacto_usuario', max_length=500, blank=True, null=True)  # Field name made lowercase.
    snombrecontacto_usuario = models.CharField(db_column='SNombreContacto_usuario', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_usuario = models.IntegerField(db_column='NEstadoRegistro_usuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
