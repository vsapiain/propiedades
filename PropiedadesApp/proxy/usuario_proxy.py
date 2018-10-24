from PropiedadesApp.models.usuario_model import Usuario
from PropiedadesApp.manager.usuario_manager import usuario_manager
#from PropiedadesApp.models.db import db

class usuario_proxy(Usuario):
    objects = usuario_manager()
    authenticated = False

    def get_by_email(self,email):
        return self.query.filter_by(Email = email).first()

    '''
    def get_all(self):
        return self.query.all()
    '''

    class Meta:
        proxy = True
