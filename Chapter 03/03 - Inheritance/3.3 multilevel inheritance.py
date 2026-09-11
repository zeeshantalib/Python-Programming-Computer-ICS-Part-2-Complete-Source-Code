# Base Class (Grandparent)
class Vehicle:
    def start_engine(self):
        print("Engine started.")

# Intermediate Class (Parent)
class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

# Derived Class (Child)
class ElectricCar(Car):
    def charge(self):
        print("Battery is charging.")

# Creating an instance of the bottom-most class
my_tesla = ElectricCar()

# Accessing methods from all levels
my_tesla.start_engine()  # Inherited from Vehicle
my_tesla.drive()         # Inherited from Car
my_tesla.charge()        # Defined in ElectricCar