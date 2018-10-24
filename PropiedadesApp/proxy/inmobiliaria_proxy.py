from PropiedadesApp.models.usuario_model import Usuario
from PropiedadesApp.manager.inmobiliaria_manager import inmobiliaria_manager

class inmobiliaria_proxy(Usuario):
    objects = inmobiliaria_manager()

    class Meta:
        proxy = True
