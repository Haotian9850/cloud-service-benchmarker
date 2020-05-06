import json 

from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import FileResponse
from geocost.S3Client import S3Client
from configs import Configs

app = FastAPI()

def get_s3_client():
    return S3Client(
        data_centers=[
            "hao-us-east-1",
            "hao-ap-southeast-2",
            "hao-ap-northeast-1",
            "hao-eu-west-2",
            "hao-sa-east-1",
            "hao-ca-central-1",
            "hao-us-west-1"
        ],
        access_key=Configs.AWS_ACCESS_KEY.value,
        secret_key=Configs.AWS_SECRET_KEY.value
    )


@app.get("/test")
def test():
    return {
        "ok": True
    }

@app.get("/download/{file_name}")
async def download(file_name:str):
    s = get_s3_client()
    s.download(
        fname=file_name,
        target_path="./geocost/temp/{}".format(file_name),
        download_patterns=[
            ("hao-us-east-1", i) for i in range(12)
        ]
    )
    return FileResponse("./geocost/temp/{}".format(file_name))

@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    content = await file.read()
    with open("./geocost/temp/{}".format(file.filename), "wb+") as fin:
        fin.write(content)
    s = get_s3_client()
    res = s.upload("./geocost/temp/{}".format(file.filename)) 
    return {
        "file_name": file.filename,
        "type": str(type(file)),
        "uploaded": res
    }