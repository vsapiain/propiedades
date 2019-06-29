from django.db import models


class Documento(models.Model):
    nid_documento = models.AutoField(db_column='NId_documento', primary_key=True)  # Field name made lowercase.
    nid_tipo_documento = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='NId_tipo_documento', blank=True, null=True)  # Field name made lowercase.
    nid_forma_pago = models.ForeignKey('FormaPago', models.DO_NOTHING, db_column='NId_forma_pago', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'documento'