from fastapi import Request, FastAPI
from starlette.staticfiles import StaticFiles

app = FastAPI()

@app.get("/items")
async def read_items(request: Request):
    return {
        "请求URL": request.url,
        "请求ip": request.client.host,
        "请求宿主": request.headers.get("user-agent"),
        "cookie": request.cookies,
    }

# 请求静态文件
"""
1.Web开发中，需要请求许多静态资源文件，如css、js、图片等，
2.这些文件通常放在static目录下，FastAPI提供了StaticFiles类来处理静态文件请求。
"""
app.mount("/static", StaticFiles(directory="static"))
