from fastapi import APIRouter
from model import *
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pathlib import Path
from tortoise.transactions import in_transaction
from numpy.ma.core import choose
from pydantic import BaseModel
student_api = APIRouter()

DIR = Path(__file__).resolve().parent.parent

@student_api.get("/", response_model_exclude={"pwd"})
async def get_All_students():
    #过滤查询
    #students = await Student.filter(class_id="14") # [Student(), Student(), ...]
    #students = await Student.get(id=6) # Student()
    #模糊查询
    #students = await Student.filter(sno__in=[2001,2002]) # [Student(), Student(), ...]
    #students = await Student.filter(sno__gt=2001) # [Student(), Student(),...]
    #values查询
    #students = await Student.all().values("name","sno") # [{'name': '张三', 'sno': 2001}, {'name': '李四', 'sno': 2002}, ...]
    # 一对多查询，多对多查询
    """
    zhangsan= await Student.get(name="zhangsan")
    await zhangsan.clas.values("name") # 班级名称

    await zhangsan.courses.all().values("name","teacher__name") # 选课的课程名称
    """
    students = await Student.all() # [Student(), Student(), ...]
    print("students:", students)
    for student in students:
        print(student.name,student.sno)
    return {"message": "List of students", "students": students}

@student_api.get("/index.html")
async def get_students_index(request: Request):
    students = await Student.all()
    templates = Jinja2Templates(directory= DIR / "templates")
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
         "students": students,
        }
    )

class Student_In(BaseModel):
    sno: int
    pwd: str
    name: str
    clas_id: int
    courses: list[int] = []

@student_api.post("/")
async def create_student(student_in: Student_In):
    #插入数据库
    student = Student(
        sno=student_in.sno,
        pwd=student_in.pwd,
        name=student_in.name,
        clas_id=student_in.clas_id
    )
    await student.save()
    #第二张方法
    # await Student.create(sno=student_in.sno,pwd=student_in.pwd,name=student_in.name,clas_id=student_in.clas_id)
    #插入多对多关系表
    choose_courses = await Course.filter(id__in=student_in.courses)
    await student.courses.add(*choose_courses)
    return {"message": "Student created", "student": student_in}

@student_api.get("/{student_id}")
async def get_student(student_id: int):
    #查询学生
    student = await Student.get(id=student_id)
    return {"message": f"Details of student {student_id}", "student": student}

# @student_api.put("/{student_id}")
# async def update_student(student_id: int, student_in: Student_In):
#     #更新学生信息
#     data = student_in.model_dump()
#     courses = data.pop("courses")
#     await Student.filter(id=student_id).update(**data)
#
#     #更新多对多关系表
#     edit_student = await Student.get(id=student_id)
#     choose_courses = await Course.filter(id__in=courses)
#     await edit_student.courses.clear()
#     await edit_student.courses.add(*choose_courses)
#
#     return edit_student

@student_api.put("/{student_id}")
async def update_student(student_id: int, student_in: Student_In):
    #改成事务，避免 clear 成功、add 失败导致关系丢失
    data = student_in.model_dump()
    courses = data.pop("courses")

    edit_student = await Student.get_or_none(id=student_id)

    choose_courses = await Course.filter(id__in=courses)

    async with in_transaction():
        await Student.filter(id=student_id).update(**data)
        await edit_student.courses.clear()
        if choose_courses:
            await edit_student.courses.add(*choose_courses)

    linked = await edit_student.courses.all().values("id", "name")
    return {"message": "updated", "id": student_id, "courses": linked}

@student_api.delete("/{student_id}")
async def delete_student(student_id: int):
    #删除学生
    student = await Student.get_or_none(id=student_id)
    if not student:
        return {"message": f"Student {student_id} not found"}
    await student.delete()

    return {"message": f"Student {student_id} deleted"}