class Teacher:
    def work(self):
        print("Teacher teaches students")


class Principal(Teacher):
    def work(self):
        print("Principal manages the school")


teacher = Teacher()
principal = Principal()

teacher.work()
principal.work()