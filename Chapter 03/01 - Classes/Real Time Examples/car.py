class Car:
    def __init__(self, company, model):
        self.company = company
        self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.company)
print(car2.model)