import requests
class PublicacionService():
    base = ""

    def get_all(self):
        request_service = requests.get(url="http://" + self.base + "/api/publicaciones/")
        request_json = request_service.json()
        request_json.update({'status': request_service.status_code})
        return request_json

    def get_code(self):
        publicaciones = self.get_all()
        publicaciones_data = publicaciones['data']
        max_code = -1
        for item in publicaciones_data:
            if item['scodigo_publicacion'] is not None:
                if int(item['scodigo_publicacion'])>max_code:
                    max_code = item['ncodigo_publicacion']
        if max_code == -1:
            max_code = 343
        return max_code + 1




