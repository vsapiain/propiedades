from PropiedadesApp.models import Usuario
from PropiedadesApp.manager.usuario_manager import usuario_manager

class UsuarioProxy(Usuario):
    objects = usuario_manager()
    authenticated = False

    def get_by_email(self,email):
        return Usuario.objects.get(email=email)

    def get_all(self):
        return Usuario.objects.all()

    class Meta:
        proxy = True
