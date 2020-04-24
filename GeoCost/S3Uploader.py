import logging
import os

import boto3
from botocore.exceptions import ClientError
from CloudStorageClient import CloudStorageClient
from Constants import Constants


class S3Uploader(CloudStorageClient):
    def upload(self, path:str) -> bool:
        if not self.client:
            self.client = boto3.client("s3")
        res = True 
        for bucket in self.data_centers:
            try:
                res = self.client.upload_file(path, bucket, os.path.basename(path))
            except ClientError as e:
                self.logger("File {} upload to S3 failed: {}...".format(path, str(e)))
                res = False
        return res

    def download(self, path:str, download_patterns:dict):
        if not self.client:
            self.client = boto3.client("s3")
        for pattern in download_patterns:
            pass

        
        

