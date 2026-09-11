class Teacher:
    def teach(self):
        print("Teaching Students")


class Student:
    def study(self):
        print("Studying Python")


class Monitor(Teacher, Student):
    def duty(self):
        print("Maintaining Discipline")


monitor = Monitor()

monitor.teach()
monitor.study()
monitor.duty()