import uvicorn
from fastapi import FastAPI
from pip._internal.commands import debug
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
from api.student import student_api
"""
aerich init -t settings.TORTOISE_ORM # TORTOISE_ORM配置的位置)
初始化完会在当前目录生成一个文件：pyproject.toml和一个文件夹：migrations
● pyproject.toml：保存配置文件路径
● migrations：存放迁移文件
"""

app = FastAPI()

app.include_router(student_api, prefix="/student", tags=["选课系统的学生接口"])
# 该方法会在fastapi启动时触发，内部通过传递进去的app对象，监听服务启动和终止事件
# 当检测到启动事件时，会初始化Tortoise对象，如果generate_schemas为True则还会进行数据库迁移
# 当检测到终止事件时，会关闭连接
register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    # generate_schemas=True,  # 如果数据库为空，则自动生成对应表单，生产环境不要开
    # add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True,workers=1, log_level="debug")  # reload=True,代码修改后会自动重启服务
