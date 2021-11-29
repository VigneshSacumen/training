
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle")
        return self.length * self.width

    def perimeter(self):
        print("Perimeter Size is:" )
        return 2 * self.length + 2 * self.width

