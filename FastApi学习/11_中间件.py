"""
FastAPI 中间件遵循 “洋葱模型” ，多个中间件的执行顺序是理解的关键。当你通过 @app.middleware("http")
或 app.add_middleware() 添加多个中间件时，它们会形成一个栈：

1.最后添加的中间件位于最外层：在请求（Request） 阶段最先执行。

2.最先添加的中间件位于最内层：在请求（Request） 阶段最后执行，最靠近你的业务逻辑。

3.响应（Response）阶段则完全相反：最先添加的（最内层）最先处理响应，最后添加的（最外层）最后处理响应。

示例：如果你依次添加了 MiddlewareA 和 MiddlewareB，那么请求路径是 Request -> B -> A -> 路由函数，
而响应路径则是 路由函数 -> A -> B -> Response
"""

import uvicorn
from fastapi import FastAPI

from fastapi import Request

import time

app = FastAPI()

"""

请求发送 -> m1 -> m2 -> 路由函数
响应接受 <- m1 <- m2 <- 路由函数
"""
@app.middleware("http")
async def m2(request: Request, call_next):  # 内层A 先添加
    # 请求代码块
    print("m2 request")
    response = await call_next(request)
    # 响应代码块
    response.headers["author"] = "yuan"
    print("m2 response")
    return response


@app.middleware("http")
async def m1(request: Request, call_next): # 外层B 后添加
    # 请求代码块
    print("m1 request")

    start = time.time()

    response = await call_next(request)
    # 响应代码块
    print("m1 response")
    end = time.time()
    response.headers["ProcessTimer"] = str(end - start)
    return response


@app.get("/user")
def get_user():
    time.sleep(3)
    print("get_user函数执行")
    return {
        "user": "current user"
    }


@app.get("/item/{item_id}")
def get_item(item_id: int):
    time.sleep(2)
    print("get_item函数执行")
    return {
        "item_id": item_id
    }


if __name__ == '__main__':
    uvicorn.run('11_中间件:app', host='127.0.0.1', port=8030, reload=True, workers=1)
