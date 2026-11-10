from fastapi import FastAPI # FastAPI是一个为你的API提供所有功能的类

app = FastAPI() # 创建FastAPI的实例对象app，是所有API的主要交互对象。这个app同样在如下的代码中被uvicorn使用

@app.get("/") # 通过装饰器@app.get()，将函数绑定到HTTP GET请求的路径上。这里的路径是"/"，表示根路径
async def root(): # 定义一个异步函数root()，它将处理根路径
    return {"message": "Hello yuan"} # 返回一个字典，FastAPI会自动将其转换为JSON格式的响应

if __name__ == "__main__":
    import uvicorn

    # 启动uvicorn服务器，指定应用程序为"main:app"，监听本地地址
    uvicorn.run("1_easy_case:app", host="127.0.0.1", port=8000, reload=True)

    # 运行后，访问http://127.0.0.1:8000/，你将看到返回的JSON响应{"message": "Hello yuan"}。
    # 你可以在浏览器中访问http://127.0.0.1:8000/docs，查看自动生成的API交互文档界面。