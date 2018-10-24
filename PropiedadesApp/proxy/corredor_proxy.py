from PropiedadesApp.models.usuario_model import Usuario
from PropiedadesApp.manager.corredor_manager import corredor_manager

class inmobiliaria_proxy(Usuario):
    objects = corredor_manager()

    class Meta:
        proxy = True
