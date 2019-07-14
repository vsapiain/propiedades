import requests
from PropiedadesApp.service.TokenService import TokenService
class PropiedadService:
    base = ""
    def add_property(self,data):
        service_token = TokenService()
        token = data['token']
        token_data = service_token.decode_token(token)
        if token_data["error"] == "0":
            request_service = requests.post(url="http://" + self.base + "/api/propiedades/", data=data,
                                            headers={'Authorization': token})
            data_service = request_service.json()
            return data_service
        return token_data