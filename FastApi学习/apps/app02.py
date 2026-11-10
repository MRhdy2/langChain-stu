from fastapi import APIRouter
from typing import Union
app02 = APIRouter()

@app02.get("/user/login")
def user_login():
    return {"user": "login"}

@app02.get("/user/reg")
def user_reg():
    return {"user": "reg"}

# 查询参数（请求参数）
@app02.get("/user/job/{kd}")
async def search_job(kd: str, city: Union[str, None] = None, xl: Union[str, None] = None):
    if city or xl:
        return {"kd": kd, "city": city, "xl": xl}
    return {"kd": kd}