class Student:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


student1 = Student()

student1.set_details("Ali", 20)
student1.show_details()