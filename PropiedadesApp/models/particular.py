from django.db import models


class Particular(models.Model):
    nid_particular = models.AutoField(db_column='NId_Particular', primary_key=True)  # Field name made lowercase.
    nid_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='NId_usuario', blank=True, null=True)  # Field name made lowercase.
    snombre_particular = models.CharField(db_column='SNombre_particular', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sapellidop_particular = models.CharField(db_column='SApellidoP_particular', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sapellidom_particular = models.CharField(db_column='SApellidoM_particular', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'particular'
