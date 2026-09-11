class Student:
    def __init__(self,name):
        self.name = name
        
    def display(self):
        print("Student Name:", self.name)

# Creating objects
object1 = Student("Ali")
object2 = Student("Ahmed")

# Using objects
object1.display()
object2.display()

