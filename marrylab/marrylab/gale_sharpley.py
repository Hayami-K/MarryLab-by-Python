class GaleSharpley:
    def __init__(self, students, laboratories):
        self.lab_dict = {lab.name: lab for lab in laboratories}
        self.student_dict = {student.id: student for student in students}
        # 配属が決定していない学生のリストを初期化
        self.free_students = set(student.id for student in students)
        self.match()

    def match(self):
        pass

