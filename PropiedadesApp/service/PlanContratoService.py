from PropiedadesApp.service.TokenService import TokenService
import requests


class PlanContratoService:
    base = ""
    def get_all(self,data):
        service_token = TokenService()
        token = data['token']
        token_data = service_token.decode_token(token)
        if token_data["error"] == "0":
            request_service = requests.get(url="http://" + self.base + "/api/planes/",
                                           params=data,
                                           headers={'Authorization': token})
            data_service =  request_service.json()
            return data_service
        return token_data

