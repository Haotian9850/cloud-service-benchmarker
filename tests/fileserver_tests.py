import requests

BASE_URL = "http://localhost:8000/"

if __name__ == "__main__":
    res = requests.post(
        url=BASE_URL + "upload",
        files={
            "file": open("./test.txt", "rb")
        },
        data={

        }
    )
    print(res.text)
