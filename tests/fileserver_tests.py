import requests
import json
import logging

BASE_URL = "http://localhost:8000/"

def upload_test():
    res = requests.post(
        url=BASE_URL + "upload",
        files={
            "file": open("./test.txt", "rb")
        },
        data={

        }
    )
    print(res.text)

def download_test():
    res = requests.get(BASE_URL + "download/test.txt")
    print(res.text)
    print(type(res.text))


if __name__ == "__main__":
    download_test()
    #upload_test()
