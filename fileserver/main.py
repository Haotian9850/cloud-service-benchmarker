import json 

from fastapi import FastAPI, Request, File, UploadFile
import geocost

app = FastAPI()

@app.get("/test")
def test():
    return {
        "ok": True
    }

@app.get("/download/{file_name}")
def download(file_name:str):
    return {
        "file_name": file_name
    }

@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    content = await file.read()
    return {
        "file_name": file.filename,
        "type": str(type(file)),
        "content": content
    }