
# Methods inside class

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print("Name: ",self.name)
        print("Age: ",self.age)


studen1=Student("Ali",20)
studen2=Student("Ahmed",22)  

studen1.show()
studen2.show()