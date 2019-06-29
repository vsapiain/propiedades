from django.db import models


class FormaPago(models.Model):
    nid_forma_pago = models.AutoField(db_column='NId_forma_pago', primary_key=True)  # Field name made lowercase.
    snombre_forma_pago = models.CharField(db_column='SNombre_forma_pago', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sdescripcion_forma_pago = models.CharField(db_column='SDescripcion_forma_pago', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nidestadoregistro_forma_pago = models.IntegerField(db_column='NIdEstadoRegistro_forma_pago', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forma_pago'
