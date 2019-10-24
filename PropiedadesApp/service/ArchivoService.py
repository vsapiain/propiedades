from django.conf import settings
import boto3
import os
#import threading

class ArchivoService:

    def copy_files_to_directory(self,files,directory):
        for file in files:
            with open(directory + file._name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

    def get_all_file_directory(self, directory):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths

    def config_s3(self):
        client = boto3.client('s3',aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,region_name=settings.AWS_S3_REGION_NAME )
        return client

    def upload_to_s3(self,file, bucket, key):
        s3 = self.config_s3()
        s3.put_object(
            ACL='public-read',
            Body=file,
            Bucket=bucket,
            Key=key
        )
        return True

    def upload_files(self,file):
        file_object = file.read()
        file_name = os.path.basename(file.name)
        if self.upload_to_s3(file_object, settings.AWS_STORAGE_BUCKET_NAME, file_name):
            return True
        else:
            return False

    def download(self):
        pass
