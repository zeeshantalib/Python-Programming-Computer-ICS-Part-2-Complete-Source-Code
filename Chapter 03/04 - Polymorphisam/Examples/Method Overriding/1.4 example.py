class Shape:
    def area(self):
        print("Area of Shape")


class Rectangle(Shape):
    def area(self):
        print("Area = Length × Width")


class Circle(Shape):
    def area(self):
        print("Area = πr²")


rectangle = Rectangle()
circle = Circle()

rectangle.area()
circle.area()