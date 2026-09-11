class Calculator:

    def add(self, *numbers):
        print(sum(numbers))


obj = Calculator()

obj.add(10, 20)
obj.add(10, 20, 30)
obj.add(10, 20, 30, 40)