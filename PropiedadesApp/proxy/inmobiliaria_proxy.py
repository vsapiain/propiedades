from PropiedadesApp.models import Usuario

class inmobiliaria_proxy(Usuario):

    class Meta:
        proxy = True
