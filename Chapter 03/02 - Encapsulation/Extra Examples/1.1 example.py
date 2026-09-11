# Without Encapsulation

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student = Student("Ali", 80)
print(student.marks)

student.marks = 500
print(student.marks)

# With Encapsulation
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

student = Student("Ali", 80)

print(student.name)
print(student.__marks)