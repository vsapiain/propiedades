from PropiedadesApp.models import  cuenta_acceso
from PropiedadesApp.models.cuenta_acceso import CuentaAcceso
from PropiedadesApp.proxy import cuenta_acceso_proxy
import jwt
import datetime
class usuario_service:
    def authenticate_user(self,tipo_usuario,password,usuario):
        token = ""
        msg = ""
        try:
            obj_cuenta = cuenta_acceso_proxy.objects.filter(semail_cuenta_acceso=usuario)
            if obj_cuenta.get(sclave_cuenta_acceso=password):
                payload = {'usuario': obj_cuenta.semail_cuenta_acceso, 'id': str(obj_cuenta.nid_cliente),
                           'tipo': '1'}
                usuario = obj_cuenta.semail_cuenta_acceso
                payload = {
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                    'iat': datetime.datetime.utcnow(),
                    'user': payload
                }
                token = jwt.encode(
                    payload,
                    "secret_citypro"
                )
            else:
                usuario = ""
                msg = "Clave de acceso incorrecta"
        except cuenta_acceso_proxy.DoesNotExist:
            msg = "Usuario no autorizado"
        user_details = {}
        user_details['username'] = usuario
        user_details['token'] = token
        user_details['msg'] = msg
        return user_details

    def is_authenticated_persona(self, email, clave):
        try:
            pass
        except ValueError:
            print("Error..." + ValueError)

    def is_authenticated_empresa(self,nombre_usuario, clave):
        pass

    def list_users(self):
        try:
            pass
        except ValueError:
            print("Error..." + ValueError)

    def encode_token(self, data_encode):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'user': data_encode
            }
            return jwt.encode(
                payload,
                "secret_citypro"
            )
        except ValueError:
            pass

    def decode_token(self, token):
        token_details = {}
        try:
            token_data = jwt.decode(token, "secret_citypro")
            token_details['token_data'] = token_data
            token_details['msg'] = ""
            token_details['err'] = "0"
            return token_details
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            token_details['token_data'] = ""
            token_details['msg'] = "La sesión a caducado"
            token_details['err'] = "1"
            return token_details