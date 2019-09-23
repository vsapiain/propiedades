from django.conf import settings
import boto3
from boto3.s3.transfer import S3Transfer
class ArchivoService:
    def config(self):
        client = boto3.client('s3',aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,region_name=settings.AWS_S3_REGION_NAME )
        return client

    def upload(self):

        nombre_archivo = "giphy.gif"
        ruta_archivo = "C:\%s" % nombre_archivo


        '''
        s3 = self.config()
        s3.upload_file(ruta_archivo,'citypro.properties',ruta_archivo)
        '''

        s3 = self.config()
        with open(ruta_archivo, 'rb') as archivo:
            s3.put_object(
                ACL='public-read',
                Body=archivo,
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=nombre_archivo
            )

        print('sali')


    def download(self):
        pass
