from PropiedadesApp.proxy import cuenta_acceso_proxy
import jwt
import datetime

class usuario_service:

    def is_authenticated_particular(self, email, clave):
        try:
            token = ""
            msg = ""
            usuario = ""
            obj_cuenta = cuenta_acceso_proxy.objects.filter(semail_cuenta_acceso=email).first()
            if obj_cuenta == None:
                msg = "Usuario no autorizado"
            else:
                if obj_cuenta.sclave_cuenta_acceso == clave:
                    payload = {'usuario': obj_cuenta.semail_cuenta_acceso, 'id': str(obj_cuenta.nid_cliente), 'tipo' : '1' }
                    usuario = obj_cuenta.semail_cuenta_acceso
                    token = self.encode_token(payload)
                else:
                    usuario=""
                    msg = "Clave de acceso incorrecta"
            user_details = {}
            user_details['username'] = usuario
            user_details['token'] = token
            user_details['msg'] = msg
            return user_details
        except ValueError:
            print("Error..." + ValueError)

    def is_authenticated_corredora(self, nombre_usuario, clave):
        pass

    def is_authenticated_inmobiliaria(self, nombre_usuario, clave):
        pass

    def encode_token(self,data_encode):
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
