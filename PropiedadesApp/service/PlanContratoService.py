from PropiedadesApp.service.TokenService import TokenService
from django.core import serializers
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
            request_json = request_service.json()
            request_json.update({'status': request_service.status_code})
            return request_json
        return token_data

