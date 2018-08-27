from PropiedadesApp.models.usuario_model import Usuario

#from PropiedadesApp.models.db import db

class usuario_proxy(Usuario):
    authenticated = False

    def get_by_email(self,email):
        return self.query.filter_by(Email = email).first()

    def get_all(self):
        return self.query.all()

    '''
    def get_model(self,Id_Usuario):
        return Usuario.get(Id_Usuario)
    '''

    class Meta:
        proxy = True
