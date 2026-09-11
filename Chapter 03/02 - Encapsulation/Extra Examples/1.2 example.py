#Reading Private Data (Getter)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

student = Student("Ali", 80)

print(student.get_marks())