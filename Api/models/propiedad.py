from django.db import models


class Propiedad(models.Model):
    nid_propiedad = models.AutoField(db_column='NId_propiedad', primary_key=True)  # Field name made lowercase.
    scodigo_propiedad = models.CharField(db_column='SCodigo_propiedad', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nid_tipo_propiedad = models.ForeignKey('TipoPropiedad', models.DO_NOTHING, db_column='NId_tipo_propiedad', blank=True, null=True)  # Field name made lowercase.
    nid_direccion = models.ForeignKey('Direccion', models.DO_NOTHING, db_column='NId_Direccion', blank=True, null=True)  # Field name made lowercase.
    ntotal_habitacion_propiedad = models.IntegerField(db_column='NTotal_habitacion_propiedad', blank=True, null=True)  # Field name made lowercase.
    ntotal_bannos_propiedad = models.IntegerField(db_column='NTotal_bannos_propiedad', blank=True, null=True)  # Field name made lowercase.
    ntotal_estacionamiento_propiedad = models.IntegerField(db_column='NTotal_estacionamiento_propiedad', blank=True, null=True)  # Field name made lowercase.
    nmts2_construido_propiedad = models.DecimalField(db_column='NMts2_construido_propiedad', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nmts2_total_propiedad = models.DecimalField(db_column='NMts2_total_propiedad', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    naireacondicionado_propiedad = models.IntegerField(db_column='NAireAcondicionado_propiedad', blank=True, null=True)  # Field name made lowercase.
    nparrilla_propiedad = models.IntegerField(db_column='NParrilla_propiedad', blank=True, null=True)  # Field name made lowercase.
    nsecadora_propiedad = models.IntegerField(db_column='NSecadora_propiedad', blank=True, null=True)  # Field name made lowercase.
    ngimnasio_propiedad = models.IntegerField(db_column='NGimnasio_propiedad', blank=True, null=True)  # Field name made lowercase.
    nlavanderia_propiedad = models.IntegerField(db_column='NLavanderia_propiedad', blank=True, null=True)  # Field name made lowercase.
    ncesped_propiedad = models.IntegerField(db_column='NCesped_propiedad', blank=True, null=True)  # Field name made lowercase.
    nmicroonda_propiedad = models.IntegerField(db_column='NMicroonda_propiedad', blank=True, null=True)  # Field name made lowercase.
    nducha_propiedad = models.IntegerField(db_column='NDucha_propiedad', blank=True, null=True)  # Field name made lowercase.
    nrefrigerador_propiedad = models.IntegerField(db_column='NRefrigerador_propiedad', blank=True, null=True)  # Field name made lowercase.
    nsauna_propiedad = models.IntegerField(db_column='NSauna_propiedad', blank=True, null=True)  # Field name made lowercase.
    npiscina_propiedad = models.IntegerField(db_column='NPiscina_propiedad', blank=True, null=True)  # Field name made lowercase.
    ntvcable_propiedad = models.IntegerField(db_column='NTVcable_propiedad', blank=True, null=True)  # Field name made lowercase.
    nlavadora_propiedad = models.IntegerField(db_column='NLavadora_propiedad', blank=True, null=True)  # Field name made lowercase.
    nwifi_propiedad = models.IntegerField(db_column='NWIfi_propiedad', blank=True, null=True)  # Field name made lowercase.
    nbodega_propiedad = models.IntegerField(db_column='NBodega_propiedad', blank=True, null=True)  # Field name made lowercase.
    ffechavigenciainicial_propiedad = models.DateTimeField(db_column='FFechaVigenciaInicial_propiedad', blank=True, null=True)  # Field name made lowercase.
    fvigenciafinal_propiedad = models.DateTimeField(db_column='FVigenciaFInal_propiedad', blank=True, null=True)  # Field name made lowercase.
    nestadoregistro_propiedad = models.IntegerField(db_column='NEstadoRegistro_propiedad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propiedad'
