import logging
import os

import boto3
from botocore.exceptions import ClientError
from CloudStorageUploader import CloudStorageUploader
from Constants import Constants


class S3Uploader(CloudStorageUploader):
    def _upload(self, path:str) -> bool:
        s3_client = boto3.client("s3")
        res = True 
        for bucket in self.data_centers:
            try:
                res = s3_client.upload_file(path, bucket, os.path.basename(path))
            except ClientError as e:
                self.logger("File {} upload to S3 failed: {}...".format(path, str(e)))
                res = False
        return res

