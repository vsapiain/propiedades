from PropiedadesApp.proxy import usuario_proxy
class usuario_service:

    def list_users(self):
        try:
            proxy = usuario_proxy()
            list_usuarios = proxy.get_all()
            return list_usuarios
        except ValueError:
            print("Error..." + ValueError)