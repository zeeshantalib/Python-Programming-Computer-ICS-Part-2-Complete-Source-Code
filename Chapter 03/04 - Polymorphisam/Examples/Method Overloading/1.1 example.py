class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


obj = Calculator()

print(obj.add(5, 10))

print(obj.add(5, 10, 20))