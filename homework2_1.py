class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Fullname: {self.fullname}, Age: {self.age}, Is married: {self.is_married}')

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super.__init__(fullname, age, is_married)
        self.marks = marks

    marks = dict
    {'object': int}

    # def marks(self):
    #     Student.marks = dict{'object': int}

    def average(self, Student_average):
        Student.average = sum(Student.marks(value))/len(Student.marks(value))

class Teacher(Person):
    def __init__(self, fullname, age, is_married, salary, base_salary):
        super.__init__(fullname, age, is_married)
        self.base_salary = base_salary
        self.salary = salary
        base_salary = 27000

    def experiences(self, experience):
        if Teacher.experience > 3:
            salary = self.base_salary + self.base_salary * 0,05


teacher = Teacher(Teacher.introduce_myself)
print(teacher)


def create_students():
    student_1 = Student('Alina', 20, 'no', {'biology': 4, 'math': 5})
    student_2 = Student('Anna', 22, 'yes', {'biology': 3, 'math': 4})
    student_3 = Student('Nadejda', 19, 'no', {'biology': 5, 'math': 3})
    students = [student_1, student_2, student_3]
    return students


for i in students:
    i.introduce_myself()
    print(i.fullname, i.age, i.is_married, i.marks)





