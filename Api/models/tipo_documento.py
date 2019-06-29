from django.db import models


class TipoDocumento(models.Model):
    nid_tipo_documento = models.AutoField(db_column='NId_tipo_documento', primary_key=True)  # Field name made lowercase.
    snombre_tipo_documento = models.CharField(db_column='SNombre_tipo_documento', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_tipo_documento = models.CharField(db_column='SDescripcion_tipo_documento', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_documento'
