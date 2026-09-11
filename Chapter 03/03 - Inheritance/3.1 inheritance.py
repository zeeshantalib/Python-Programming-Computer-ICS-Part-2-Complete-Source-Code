# Parent class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


# Child class (Subclass) inheriting from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")


# Create an object of the child class
my_dog = Dog("Buddy")

# Access method from Parent class
my_dog.eat()   # Output: Buddy is eating.

# Access method from Child class
my_dog.bark()  # Output: Buddy says Woof!