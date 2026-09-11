# Updating Private Data (Setter)
class Student:
    def __init__(self, name, marks):
        self.__marks = marks

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

student = Student("Ali", 80)

student.set_marks(90)
print(student.get_marks())