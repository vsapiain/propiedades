from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='Id_Usuario', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    clave = models.CharField(db_column='Clave', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'
