from django.db import models


class Cliente(models.Model):
    nid_cliente = models.AutoField(db_column='NId_cliente', primary_key=True)  # Field name made lowercase.
    nid_tipo_cliente = models.ForeignKey('TipoCliente', models.DO_NOTHING, db_column='NId_tipo_cliente', blank=True, null=True)  # Field name made lowercase.
    nid_direccion = models.ForeignKey('Direccion', models.DO_NOTHING, db_column='NId_Direccion', blank=True, null=True)  # Field name made lowercase.
    nrut_cliente = models.IntegerField(db_column='NRut_cliente', blank=True, null=True)  # Field name made lowercase.
    srutdigito_cliente = models.CharField(db_column='SRutDigito_cliente', max_length=10, blank=True, null=True)  # Field name made lowercase.
    srut_cliente = models.CharField(db_column='SRut_cliente', max_length=10, blank=True, null=True)  # Field name made lowercase.
    semailcontacto_cliente = models.CharField(db_column='SEmailContacto_cliente', max_length=500, blank=True, null=True)  # Field name made lowercase.
    snombrecontacto_cliente = models.CharField(db_column='SNombreContacto_cliente', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_cliente = models.IntegerField(db_column='NEstadoRegistro_cliente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'
