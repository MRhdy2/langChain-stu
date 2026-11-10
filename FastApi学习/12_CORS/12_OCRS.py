from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:63342"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # *：代表所有客户端
    allow_credentials=True,
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    print("hello world")
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("12_OCRS:app", host="127.0.0.1", port=8000, log_level="debug", reload=True)
