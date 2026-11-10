from fastapi import FastAPI, Form
import uvicorn

app = FastAPI()

@app.post("/regin")
def regin(username: str = Form(...,max_length=16,min_length=8, pattern='[a-zA-Z]'),
          password: str = Form(..., max_length=16, min_length=8, pattern='[a-zA-Z]')):
    print(f"username: {username}, password: {password}")

    return {"username": username, "password": password}
if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)