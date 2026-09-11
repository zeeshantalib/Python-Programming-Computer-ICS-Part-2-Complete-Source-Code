class Animal:
    def sound(self):
        return "Some generic sound"


class Dog(Animal):
    def sound(self): 
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.sound())