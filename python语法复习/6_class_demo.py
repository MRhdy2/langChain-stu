class Student(object):
    def __init__(self, name, stu_number):
        self.name = name
        self.stu_number = stu_number
        self.grade = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, subject, score):
        if subject in self.grade:
            self.grade[subject] = score
        else:
            print("科目不存在")

    def score_print(self):
        print(f"数学成绩为{self.grade['数学']}")
        print(f"语文成绩为{self.grade['语文']}")
        print(f"英语成绩为{self.grade['英语']}")
stu1 = Student("张三", "2023001")
stu1.set_grade("数学", 90)
stu1.set_grade("语文", 85)
stu1.set_grade("英语", 88)
stu1.score_print()