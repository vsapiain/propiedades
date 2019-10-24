from django.core import serializers
from PropiedadesApp.service.ArchivoService import ArchivoService
import uuid
import zipfile
import os
from os import remove
from PIL import Image, ImageDraw, ImageFont

class ImagenService:


    def upload(self,files):
        ok = False
        archivo_service = ArchivoService()
        #directorio_temporal = 'C:\\Temp\\'
        directorio_temporal = "Temp/"
        os.makedirs(directorio_temporal, exist_ok=True)
        uid = uuid.uuid1().hex
        archivo_service.copy_files_to_directory(files,directorio_temporal)
        file_paths = archivo_service.get_all_file_directory(directorio_temporal)

        for file in file_paths:
            foo = Image.open(file)
            foo = foo.resize((600, 400), Image.ANTIALIAS)
            foo.save(file, optimize=True, quality=80)

        with zipfile.ZipFile(directorio_temporal + 'archivo.zip', 'w') as zip:
            for file in file_paths:
                zip.write(file,arcname=os.path.basename(file))
                remove(file)
        zip.close()

        with open(directorio_temporal + 'archivo.zip', 'rb') as f:
            if archivo_service.upload_files(f):
                f.closed
                ok = True
        if ok:
            # guardar en bd
            remove(directorio_temporal + 'archivo.zip')
