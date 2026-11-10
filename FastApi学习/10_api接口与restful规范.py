"""
应用程序编程接口（Application Programming Interface，API接口），就是应用程序对外提供了一个操作数据的入口

只要API程序遵循了REST风格，那就可以称其为RESTful API。目前在前后端分离的架构中，前后端基本都是通过RESTful API来进行交互。
REST的含义就是客户端与Web服务器之间进行交互的时候，使用HTTP协议中的4个请求方法代表不同的动作。
GET用来获取资源
POST用来新建资源
PUT用来更新资源
DELETE用来删除资源。
"""
from fastapi.exceptions import HTTPException


from FastApi学习.model import Course, Student
from pydantic import BaseModel
from typing import List, Union
from fastapi import APIRouter

api_student = APIRouter()


@api_student.get("/student")
async def getAllStudent():
    students = await Student.all().values("name", "clas__name")
    # students = await Student.filter(name__icontains='a').values("name", "clas__name")
    # print("students", students)
    # for i in students:
    #     print(i)
    #
    # rain = await Student.get(name='rain')
    # print(rain, type(rain))
    # print(rain.sno)

    return students


class StudentModel(BaseModel):
    name: str
    pwd: str
    sno: int
    clas_id: Union[int, None] = None
    courses: List[int] = []


@api_student.post("/student")
async def addStudent(stu: StudentModel):
    # 添加数据库操作
    # 方式1
    # student = Student(name=stu.name, pwd=stu.pwd, sno=stu.sno, clas_id=stu.clas)
    # await student.save()
    # 方式2
    student = await Student.create(name=stu.name, pwd=stu.pwd, sno=stu.sno, clas_id=stu.clas_id)
    print(student, dir(student))

    # 添加多对多关系记录
    courses = await Course.filter(id__in=stu.courses)
    print("courses", courses)
    await student.courses.add(*courses)
    print("student", student.courses)

    return student


@api_student.put("/student/{student_id}")
async def update_student(student_id: int, student: StudentModel):
    data = student.dict(exclude_unset=True)
    courses = data.pop("courses")
    print(data, courses)
    await Student.filter(id=student_id).update(**data)

    courses = await Course.filter(id__in=student.courses)
    edit_student = await Student.get(id=student_id)
    await edit_student.courses.clear()
    await edit_student.courses.add(*courses)

    return student


@api_student.delete("/student/{student_id}")
async def delete_student(student_id: int):
    deleted_count = await Student.filter(id=student_id).delete()  # 条件删除
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Student {student_id} not found")
    return {}
