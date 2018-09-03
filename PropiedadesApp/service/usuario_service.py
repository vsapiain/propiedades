from PropiedadesApp.models.usuario_model import Usuario
from PropiedadesApp.proxy.usuario_proxy import usuario_proxy

class usuario_service:
    def is_authenticated(self,_email,_clave):
        try:
            proxy  = usuario_proxy()
            obj_usuario = proxy.get_by_email(_email)
            if obj_usuario == None:
                return usuario_proxy(),'Correo electronico no registrado.'
            else:
                if obj_usuario.Clave != _clave:
                    return usuario_proxy(),'Clave de acceso incorrecta.'
                else:
                    proxy.authenticated = True
                    return obj_usuario, ''
        except:
            pass

    def __init__(self):
        pass
