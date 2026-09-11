# Vehicle Hierarchy
class Vehicle:
    def start(self):
        print("Vehicle Started")


class Car(Vehicle):
    def drive(self):
        print("Driving Car")


class SportsCar(Car):
    def turbo(self):
        print("Turbo Mode Enabled")


car = SportsCar()

car.start()
car.drive()
car.turbo()