import requests

class ComunaService:
    base = ""
    def get_all(self):
        comuna_data = {}
        request_service = requests.post(url="http://" + self.base + "/api/comunas/")
        data =  request_service.json()
        return data


