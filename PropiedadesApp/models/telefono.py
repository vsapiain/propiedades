from django.db import models


class Telefono(models.Model):
    nid_telefono = models.AutoField(db_column='NId_telefono', primary_key=True)  # Field name made lowercase.
    nid_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='NId_usuario', blank=True, null=True)  # Field name made lowercase.
    snumero_telefono = models.CharField(db_column='SNumero_telefono', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nestado_registro = models.IntegerField(db_column='NEstado_Registro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'telefono'
