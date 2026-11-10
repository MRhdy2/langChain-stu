from fastapi import FastAPI, File, UploadFile
from typing import List
import uvicorn

app = FastAPI()

# file: bytes = File(): 适合小文件上传
@app.post("/file/")
async def create_file(file: bytes = File()):
    print("file:", file)
    return {"file_size": len(file)}

@app.post("/multifiles/")
async def create_files(files: List[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}

# file: UploadFile 适合大文件上传
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    with open(f"{file.filename}", "wb") as f:
        for chunk in iter(lambda: file.file.read(1024), b""):
            f.write(chunk)
    return {"filename": file.filename}

@app.post("/multiuploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}

if __name__ == "__main__":
    original_openapi = app.openapi


    def custom_openapi():
        schema = original_openapi()
        for model in schema.get("components", {}).get("schemas", {}).values():
            for field in model.get("properties", {}).values():
                items = field.get("items")
                if (
                        isinstance(items, dict)
                        and items.get("contentMediaType") == "application/octet-stream"
                ):
                    items["format"] = "binary"
        return schema


    app.openapi = custom_openapi
    uvicorn.run("5_文件上传:app", host="127.0.0.1", port=8000, reload=True)