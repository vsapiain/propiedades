import jwt
import datetime

class TokenService:

    def encode_token(self, data_encode):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=60 * 30),
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
            token_details['id'] = token_data['user']['id']
            token_details['plan'] = token_data['user']['plan']
            token_details['plan_id'] = token_data['user']['plan_id']
            token_details['planLink'] = token_data['user']['planLink']
            token_details['msg'] = ""
            token_details['error'] = "0"
            token_details['token'] = token
            return token_details
        except (jwt.ExpiredSignatureError):
            token_details['username'] = ""
            token_details['id'] = ""
            token_details['msg'] = "La sesión a caducado"
            token_details['error'] = "1"
            token_details['token'] = ""
            return token_details
        except (jwt.DecodeError):
            token_details['username'] = ""
            token_details['id'] = ""
            token_details['msg'] = "Token invalido"
            token_details['error'] = "1"
            token_details['token'] = ""
            return token_details