   # very basic class concept

class Student:
    age=30
    def show(self): 
        print("i am a show function")

student1 = Student()

print(student1.age)  # Outputs: 30
student1.show()      # Outputs: i am a show function
