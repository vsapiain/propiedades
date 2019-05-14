from PropiedadesApp.models import Usuario

class InmobiliariaProxy(Usuario):

    class Meta:
        proxy = True
