#from PropiedadesApp.proxy import cuenta_acceso_proxy
from Api.proxy import  cuenta_acceso_proxy
import jwt
import datetime

class usuario_service:
    def is_authenticated_particular(self, email, clave):
        try:
            token = ""
            msg = ""
            usuario = ""
            tipo_cliente_paticular = 1
            try:
                obj_cuenta = cuenta_acceso_proxy.objects.filter(nid_cliente__nid_tipo_cliente=tipo_cliente_paticular).\
                    filter(semail_cuenta_acceso=email).get()
                if obj_cuenta.sclave_cuenta_acceso == clave:
                    payload = {'username': obj_cuenta.semail_cuenta_acceso, 'id': str(obj_cuenta.nid_cliente), 'tipo': str(tipo_cliente_paticular)}
                    usuario = obj_cuenta.semail_cuenta_acceso
                    token = self.encode_token(payload)
                else:
                    usuario = ""
                    msg = "Clave de acceso incorrecta"
            except cuenta_acceso_proxy.DoesNotExist:
                msg = "Usuario no autorizado"
            user_details = {}
            user_details['username'] = usuario
            user_details['token'] = token
            user_details['msg'] = msg
            user_details['error'] = ""
            return user_details
        except ValueError:
            return None

    def is_authenticated_corredora(self, nombre_usuario, clave):
        try:
            token = ""
            msg = ""
            usuario = ""
            tipo_cliente_corredora = 2
            try:
                obj_cuenta = cuenta_acceso_proxy.objects.filter(nid_cliente__nid_tipo_cliente=tipo_cliente_corredora). \
                    filter(snombreusuario_cuenta_acceso=nombre_usuario).get()
                if obj_cuenta.sclave_cuenta_acceso == clave:
                    payload = {'usuario': obj_cuenta.snombreusuario_cuenta_acceso, 'id': str(obj_cuenta.nid_cliente),
                               'tipo': str(tipo_cliente_corredora)}
                    usuario = obj_cuenta.snombreusuario_cuenta_acceso
                    token = self.encode_token(payload)
                else:
                    usuario = ""
                    msg = "Clave de acceso incorrecta"
            except cuenta_acceso_proxy.DoesNotExist:
                msg = "Usuario no autorizado"
            user_details = {}
            user_details['username'] = usuario
            user_details['token'] = token
            user_details['msg'] = msg
            user_details['error'] = "0"
            return user_details
        except ValueError:
            user_details = {}
            user_details['username'] = ""
            user_details['token'] = ""
            user_details['msg'] = "Error inesperable"
            user_details['error'] = "1"

    def is_authenticated_inmobiliaria(self, nombre_usuario, clave):
        try:
            token = ""
            msg = ""
            usuario = ""
            tipo_cliente_inmobiliaria = 3
            try:
                obj_cuenta = cuenta_acceso_proxy.objects.filter(nid_cliente__nid_tipo_cliente=tipo_cliente_inmobiliaria). \
                    filter(snombreusuario_cuenta_acceso=nombre_usuario).get()
                if obj_cuenta.sclave_cuenta_acceso == clave:
                    payload = {'usuario': obj_cuenta.snombreusuario_cuenta_acceso, 'id': str(obj_cuenta.nid_cliente),
                               'tipo': str(tipo_cliente_inmobiliaria)}
                    usuario = obj_cuenta.snombreusuario_cuenta_acceso
                    token = self.encode_token(payload)
                else:
                    usuario = ""
                    msg = "Clave de acceso incorrecta"
            except cuenta_acceso_proxy.DoesNotExist:
                msg = "Usuario no autorizado"
            user_details = {}
            user_details['username'] = usuario
            user_details['token'] = token
            user_details['msg'] = msg
            user_details['error'] = ""
            return user_details
        except ValueError:
            return None

    def encode_token(self,data_encode):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=60*30),
                'iat': datetime.datetime.utcnow(),
                'user': data_encode
            }
            return jwt.encode(
                payload,
                "secret_citypro"
            )
        except ValueError:
            return None

    def decode_token(self, token):
        token_details = {}
        try:
            token_data = jwt.decode(token, "secret_citypro")
            token_details['username'] = token_data['user']['username']
            token_details['msg'] = ""
            token_details['error'] = "0"
            token_details['token'] = token
            return token_details
        except (jwt.ExpiredSignatureError):
            token_details['username'] = ""
            token_details['msg'] = "La sesión a caducado"
            token_details['error'] = "1"
            token_details['token'] = ""
            return token_details
        except (jwt.DecodeError):
            token_details['username'] = ""
            token_details['msg'] = "Token invalido"
            token_details['error'] = "1"
            token_details['token'] = ""
            return token_details
