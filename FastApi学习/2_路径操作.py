"""
@app.include_router() 方法用于将一个路由器（Router）包含到主应用程序中。它允许你将不同的路由器组织在一起，并为它们指定前缀和标签。
参数说明：
- router: 要包含的路由器对象。
- prefix: 可选参数，指定路由器的前缀路径。所有路由器中的路由将以该前缀开头。
- tags: 可选参数，用于为路由器中的路由添加标签。

@app.get() 方法用于定义一个 GET 请求的路由。它用于处理客户端发送的 GET 请求，并返回相应的响应。
@app.post() 方法用于定义一个 POST 请求的路由。它用于处理客户端发送的 POST 请求，并返回相应的响应。
@app.put() 方法用于定义一个 PUT 请求的路由。它用于处理客户端发送的 PUT 请求，并返回相应的响应。
@app.delete() 方法用于定义一个 DELETE 请求的路由。它用于处理客户端发送的 DELETE 请求，并返回相应的响应。
@app.patch() 方法用于定义一个 PATCH 请求的路由。它用于处理客户端发送的 PATCH 请求，并返回相应的响应。
@app.options() 方法用于定义一个 OPTIONS 请求的路由。它用于处理客户端发送的 OPTIONS 请求，并返回相应的响应。
@app.head() 方法用于定义一个 HEAD 请求的路由。它用于处理客户端发送的 HEAD 请求，并返回相应的响应。
@app.trace() 方法用于定义一个 TRACE 请求的路由。它用于处理客户端发送的 TRACE 请求，并返回相应的响应。
@app.post(
    "/items/{item_id}", # 路径参数
    response_model=Item, # 响应模型
    status_code=status.HTTP_200_OK, # 响应状态码
    tags=["AAA"],  # 标题
    summary="this is summary", # 摘要
    description="this is description", # 描述
    response_description= "this is response_description", # 响应描述
    deprecated=False, # 这个接口是否弃用
)
"""


from typing import Union
from fastapi import FastAPI
import uvicorn
from apps import app01, app02

app = FastAPI()

app.include_router(app01, prefix="/app01", tags=["第一章节：商城接口"])
app.include_router(app02, prefix="/app02", tags=["第二章节：用户中心接口"])

if __name__ == "__main__":

    uvicorn.run("2_路径操作:app", host="127.0.0.1", port=8000, reload=True)
