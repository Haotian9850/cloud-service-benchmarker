import logging
import os

import boto3
from botocore.exceptions import ClientError
from CloudStorageClient import CloudStorageClient


class S3Client(CloudStorageClient):
    def upload(self, path:str) -> bool:
        self._validate_path(path)
        partitions = self.fsplitter.split_and_save(path)
        print(partitions)
        res = True
        for fpart in partitions:
            res = self._upload_single_file("{}/{}".format(self.temp_path, fpart))
        if not res:
            self.logger.warning("Some parition of file {} was not successfully uploaded to S3...".format(path))
        return res


    def download(self, path:str, download_patterns:dict):
        if not self.client:
            self.client = boto3.client("s3")
        for pattern in download_patterns:
            pass

    def _upload_single_file(self, fpath) -> bool:
        if not self.client:
            self.client = self._get_s3_client()
        res = True 
        for bucket in self.data_centers:
            try:
                self.logger.info("Uploading {} to {}...".format(fpath, bucket))
                self.client.upload_file(
                    fpath,
                    bucket,
                    os.path.basename(fpath)
                )
            except ClientError as e:
                self.logger.error("Uploading of {} failed: {}".format(fpath, str(e)))
                res = False 
        return res


    def _get_s3_client(self):
        return boto3.client(
            "s3",
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )
        
        

