from typing import Union, List,Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field,ValidationError,field_validator
import uvicorn
from datetime import date

# class Addr(BaseModel):
#     province: str
#     city: str

class User(BaseModel):
    name: str = 'root'
    age: int =Field(default=0,lt=100,gt=0) # 年龄，必须在0-100之间
    birth: Optional[date] = None # 出生日期
    friends: List[str] = [] # 朋友列表
    description: Union[str, None] = None

    # addr: Union[Addr, None] = None # 类型嵌套
    @field_validator('name')
    @classmethod
    def name_must_be_alpha(cls, v):
        assert v.isalpha(), 'must be only alpha'
        return v

class Data(BaseModel):
    user: List[User] = [] # 用户列表

app = FastAPI()

@app.post("/data/")
async def create_data(data: Data):
    # 添加数据库
    return data

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
"""
测试数据
{
  "name": "rain",
  "age": 32,
  "birth": "1990-09-29",
  "friends": ["jack", "tom"],
  "description": "最帅的讲fastapi的老师"
}
"""
