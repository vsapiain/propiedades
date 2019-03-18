from django.db import models


class CuentaAcceso(models.Model):
    nid_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='NId_cliente')  # Field name made lowercase.
    nid_cuenta_acceso = models.IntegerField(db_column='NId_cuenta_acceso', blank=True, primary_key=True)  # Field name made lowercase.
    snombreusuario_cuenta_acceso = models.CharField(db_column='SNombreUsuario_cuenta_acceso', max_length=500,blank=True, null=True) # Field name made lowercase.
    semail_cuenta_acceso = models.CharField(db_column='SEmail_cuenta_acceso', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sclave_cuenta_acceso = models.CharField(db_column='SClave_cuenta_acceso', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ffechavigenciainicial_cuenta_acceso = models.DateTimeField(db_column='FFechaVigenciaInicial_cuenta_acceso', blank=True, null=True)  # Field name made lowercase.
    ffechavigenciafinal_cuenta_acceso = models.DateTimeField(db_column='FFechaVigenciaFinal_cuenta_acceso', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_cuenta_acceso = models.IntegerField(db_column='NEstadoRegistro_cuenta_acceso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta_acceso'
