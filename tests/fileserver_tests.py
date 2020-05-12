import requests
import json
import time
import os
import logging
import boto3

from configs import Configs

BUCKET = "hao-us-east-1"

BASE_URL = "http://localhost:8000/"

def upload_test():
    res = requests.post(
        url=BASE_URL + "upload",
        files={
            "file": open("./test_files/10mb.txt", "rb")
        },
        data={

        }
    )
    print(res.text)

def download_test_split():
    start = time.time()
    res = requests.get(BASE_URL + "download/10mb.txt")
    if res.text:
        print("Downloading test complete...")
    end = time.time()
    return end - start

def download_test_single(fpath, upload=False):
    client = boto3.client(
        "s3",
        aws_access_key_id=Configs.AWS_ACCESS_KEY.value,
        aws_secret_access_key=Configs.AWS_SECRET_KEY.value
    )
    if upload:
        print("uploading...")
        client.upload_file(
            fpath,
            BUCKET,
            os.path.basename(fpath)
        )
    start = time.time()
    client.download_file(
        BUCKET,
        "10mb.txt",
        "./dump/dump.txt"
    )
    end = time.time()
    print("Single file downloading complete...")
    return end - start

    


if __name__ == "__main__":
    
    upload_test()
    temp = list()
    for i in range(100):
        temp.append(download_test_split())
    print(str(temp))
    '''
    download_test_single("./test_files/10mb.txt", upload=True)
    temp = list()
    for i in range(100):
        temp.append(download_test_single("./test_files/10mb.txt"))
    print(str(temp))
    '''
