class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result


# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())       # Output: 1
print(calc.multiply(4))      # Output: 4

# Using multiple arguments
print(calc.multiply(2, 3))    # Output: 6
print(calc.multiply(2, 3, 4)) # Output: 24