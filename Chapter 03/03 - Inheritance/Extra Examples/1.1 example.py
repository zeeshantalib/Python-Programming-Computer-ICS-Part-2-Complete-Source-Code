# Basic (Single Inheritance)

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def show_student(self):
        self.show_name()
        print("Roll No:", self.roll_no)

student = Student("Ali", "CS-101")
student.show_student()
