import boto3

class ArchivoService:
    def config(self):
        client = boto3.client('s3',aws_access_key_id="AKIAYBGDREPHT47B2KPG",
                      aws_secret_access_key="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",region_name='us-east-2' )
        return client

    def upload(self):

        nombre_archivo = "giphy.gif"
        ruta_archivo = "C:\%s" % nombre_archivo
        s3 = self.config()
        s3.upload_file(ruta_archivo,'citypro.properties',ruta_archivo)
        print ('ok')
        '''
        with open(ruta_archivo, 'rb') as archivo:
            client.put_object(
                ACL='public-read',
                Body=archivo,
                Bucket='citypro.properties',
                Key=nombre_archivo
            )
        '''

        '''
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
            print(bucket.name)
        '''
    def download(self):
        pass
