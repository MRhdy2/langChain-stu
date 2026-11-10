"""
FASTAPI提供了response_model参数来定义return响应体模型
#路径操作
@app.get("/items/{item_id}", response_model=Item)
#路径函数
async def read_item(item_id: int):
    ...
FastAPI将使用response_model进行以下操作：
● 将输出数据转换为response_model中声明的数据类型。
● 验证数据结构和类型
● 将输出数据限制为该model定义的
● 添加到OpenAPI中
● 在自动文档系统中使用。
response_model_exclude_unset=True,不会返回默认值,忽略未设置的默认字段
response_model_exclude_defaults=False,会返回默认值
"""
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None
#@app.post("/user/",  response_model=UserOut,response_model_exclude={"password"}) 会忽略password字段,不会返回password字段
#@app.post("/user/",  response_model=UserOut,response_model_include={"username","email"}) 会只返回username和email字段,不会返回其他字段
#@app.post("/user/",  response_model=UserOut,response_model_exclude_unset=False) 不会忽略未设置的默认字段,会返回默认值
@app.post("/user/",  response_model=UserOut,response_model_exclude_unset=True) #会忽略未设置的默认字段,不会返回默认值
async def create_user(user: UserIn):
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)