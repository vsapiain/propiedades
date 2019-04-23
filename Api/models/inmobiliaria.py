from django.db import models


class Inmobiliaria(models.Model):
    nid_inmobiliaria = models.AutoField(db_column='NId_inmobiliaria', primary_key=True)  # Field name made lowercase.
    nid_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='NId_usuario', blank=True, null=True)  # Field name made lowercase.
    snombre_inmobiliaria = models.CharField(db_column='SNombre_inmobiliaria', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inmobiliaria'
