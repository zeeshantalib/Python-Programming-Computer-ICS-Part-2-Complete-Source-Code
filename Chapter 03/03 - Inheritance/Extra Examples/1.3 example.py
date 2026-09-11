# Person Hierarchy
class Person:
    def show_person(self):
        print("I am a Person")


class Teacher(Person):
    def show_teacher(self):
        print("I am a Teacher")


class Principal(Teacher):
    def show_principal(self):
        print("I am the Principal")


principal = Principal()

principal.show_person()
principal.show_teacher()
principal.show_principal()