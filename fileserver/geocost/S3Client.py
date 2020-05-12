import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

import boto3
from botocore.exceptions import ClientError
from geocost.CloudStorageClient import CloudStorageClient


class S3Client(CloudStorageClient):
    def upload(self, path:str) -> bool:
        self._validate_path(path)
        partitions = self.fsplitter.split_and_save(path)
        res = True
        for fpart in partitions:
            res = self._upload_single_file("{}/{}".format(self.temp_path, fpart))
        if not res:
            self.logger.warning("Some parition of file {} was not successfully uploaded to S3...".format(path))
        return res

    '''
    @ PARAMS:
    download_patterns:[(bucket, partition_number),...]
    '''
    def download(self, fname:str, target_path:str, download_patterns:dict):
        self._validate_download_pattern(download_patterns)
        if not self.client:
            self.client = self._get_s3_client()
        with ThreadPoolExecutor(max_workers=12) as t:
            all_jobs = [
                t.submit(
                    self.client.download_file,
                    Key="{}_{}".format(fname, pattern[1]),
                    Filename="{}/{}_{}".format(self.temp_path, fname, pattern[1]),
                    Bucket=pattern[0]
                ) for pattern in download_patterns
            ]
        for _ in as_completed(all_jobs):
            self.logger.info("Download task completed...")
        '''
        for pattern in download_patterns:
            self.logger.info("Downloading parition {} from {}...".format(pattern[1], pattern[0]))
            self.client.download_file(
                pattern[0],
                "{}_{}".format(fname, pattern[1]),
                "{}/{}_{}".format(self.temp_path, fname, pattern[1])
            )
        '''
        self.logger.info("Merging partitions...")
        self.fappender.merge_partitions(
            filename=fname,
            target_path=target_path
        )
        self.logger.info("{} partitions successfully merged...".format(len(download_patterns)))
        
            

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
        
        

