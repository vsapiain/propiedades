from Api.models import CuentaAcceso
from PropiedadesApp.service.TokenService import TokenService
import jwt
import requests

class UsuarioService:
    base = ""

    def authenticate_user(self, data):
        request_service = requests.post(url="http://" + self.base + "/api/authenticate_user/", data=data)
        data_service = request_service.json()
        if data_service["error"] == 1:
            resp = {"token": "", "error": "1", "msg": data_service["msg"], "username": ""}
        else:
            resp = {"token": data_service["token"], "error": 0, "msg": data_service["msg"],
                    "username": data_service["username"]}
        return resp

    def get_user(self, data):
        service_token = TokenService()
        token = data['token']
        token_data = service_token.decode_token(token)
        if token_data["error"] == "0":
            id = token_data["id"]
            request_service = requests.get(url="http://" + self.base + "/api/usuarios/" + str(id),
                                           headers={'Authorization': token})
            data_service = request_service.json()
            return data_service
        return token_data

    def set_user(self, data):
        service_token = TokenService()
        token = data['token']
        token_data = service_token.decode_token(token)
        if token_data["error"] == "0":
            id = token_data["id"]
            request_service = requests.put(url="http://" + self.base + "/api/usuarios/" + str(id), data = data,
                                           headers={'Authorization': token})
            request_json = request_service.json()
            request_json.update({'status': request_service.status_code})
        return request_json

    def set_account_password(self, data):
        service_token = TokenService()
        token = data['token']
        token_data = service_token.decode_token(token)
        id = token_data["id"]
        clave = data["clave"]
        clave_nueva = data["ClaveNueva"]
        obj_cuenta = CuentaAcceso.objects.filter(nid_cuenta_acceso=int(id)).get()
        if token_data["error"] == "0":
            if obj_cuenta.sclave_cuenta_acceso != clave:
                token_data["error"] = "1"
                token_data["msg"] = "Clave actual incorrecta"
                return token_data
            else:
                usuario =  obj_cuenta.snombre_cuenta_acceso
                FVigenciaInicial = obj_cuenta.ffechavigenciainicial_cuenta_acceso
                FVigenciaFinal = obj_cuenta.ffechavigenciafinal_cuenta_acceso
                email = obj_cuenta.semail_cuenta_acceso
                data_account ={"usuario":usuario,"FVigenciaInicial":FVigenciaInicial,"FVigenciaFinal":FVigenciaFinal,
                               "email":email,"clave":clave_nueva}
                request_service = requests.put(url="http://" + self.base + "/api/cuentas/" + str(id), data=data_account,
                                               headers={'Authorization': token})
                request_json = request_service.json()
                request_json.update({'status': request_service.status_code})
                return request_json
        return token_data