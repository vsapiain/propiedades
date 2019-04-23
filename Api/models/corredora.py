from django.db import models


class Corredora(models.Model):
    nid_corredora = models.AutoField(db_column='NId_corredora', primary_key=True)  # Field name made lowercase.
    nid_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='NId_usuario', blank=True, null=True)  # Field name made lowercase.
    srazonsocial_corredora = models.CharField(db_column='SRazonSocial_corredora', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    snombre_corredora = models.CharField(db_column='SNombre_corredora', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    snombrecontacto_corredora = models.CharField(db_column='SNombreContacto_corredora', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'corredora'
