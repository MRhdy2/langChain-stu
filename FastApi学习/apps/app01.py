from fastapi import APIRouter

app01 = APIRouter()

@app01.get("/shop/food")
def shop_food():
    return {"shop": "food"}

@app01.get("/shop/bed")
def shop_bed():
    return {"shop": "bed"}

#路径参数
#1.有类型路径参数
@app01.get("/shop/{shop_id}")
def shop_id(shop_id: int):
    print(shop_id,type(shop_id))
    return {"shop_id": shop_id}

#2.有类型路径参数+默认值
@app01.get("/shop/{shop_id}")
def shop_id_name(shop_id: int, shop_name: str = "默认值"):
    print(shop_id,type(shop_id))
    print(shop_name,type(shop_name))
    return {"shop_id": shop_id, "shop_name": shop_name}

#3.顺序传参
@app01.get("/user/me")
async def read_user_me():
    return {"username": "the current user"}

@app01.get("/user/{username}")
async def read_user(username: str):
    return {"username": username}
