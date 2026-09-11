# Parent Class 1
class Father:
    def skill1(self):
        print("Father's skill: Gardening")


# Parent Class 2
class Mother:
    def skill2(self):
        print("Mother's skill: Cooking")


# Derived class inheriting from two base classes (Multiple Inheritance)
class Child(Father, Mother):
    def own_skill(self):
        print("Child's skill: Coding")


# Creating an instance of Child
child = Child()

# Accessing Father's method
child.skill1()

# Accessing Mother's method
child.skill2()

# Accessing its own method
child.own_skill()