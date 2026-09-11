class Student:
    def __init__(self, name, roll_no, password):
        self.name = name              # Public
        self._roll_no = roll_no       # Protected
        self.__password = password    # Private

    def show_details(self):
        print("Name:", self.name)
        print("Roll No:", self._roll_no)
        print("Password:", self.__password)

student = Student("Ali", "CS-101", "Ali@123")

print(student.name)
print(student._roll_no)
# print(student.__password)   # Error

student.show_details()