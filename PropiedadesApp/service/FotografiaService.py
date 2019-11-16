import zipfile
import os
import json
import requests
from os import remove
from django.core import serializers
from PropiedadesApp.service.ArchivoService import ArchivoService
from PropiedadesApp.service.TokenService import TokenService

class FotografiaService:
    base = ""
    def upload(self,files,bucket_path='',codigo=''):
        resp = False
        ok = False
        archivo_service = ArchivoService()
        quality_image = 80
        directorio_temporal = 'Temp/'
        os.makedirs(directorio_temporal, exist_ok=True)
        archivo_service.copy_files_to_directory(files,directorio_temporal)
        file_paths = archivo_service.get_all_file_directory(directorio_temporal)
        for file in file_paths:
            archivo_service.optimize_image(file,quality_image)
        with zipfile.ZipFile(directorio_temporal + codigo + '.zip', 'w') as zip:
            for file in file_paths:
                zip.write(file,arcname=os.path.basename(file))
                remove(file)
        zip.close()

        with open(directorio_temporal + codigo + '.zip', 'rb') as f:
            if archivo_service.upload_files(f,bucket_path):
                f.closed
                ok = True
        if ok:
            remove(directorio_temporal + codigo + '.zip')
            resp = True
        return resp

    def save(self,data):
        service_token    = TokenService()
        token = data['token']
        token_data = service_token.decode_token(token)
        id_publicacion = data['publicacion']
        if token_data["error"] == "0":
            request_service = requests.post(url='http://' + self.base + '/api/publicaciones/' + str(id_publicacion) +'/fotografias/', data=data,headers={'Authorization': token})

        #data = json.dumps(files_list)
