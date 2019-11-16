import requests

class ComunaService:
    base = ""
    def get_all(self):
        request_service = requests.get(url="http://" + self.base + "/api/comunas/")
        request_json =  request_service.json()
        request_json.update({'status' : request_service.status_code})
        return request_json



