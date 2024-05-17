'''22.Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length = 5
width = 3
rectangle = Rectangle(length, width)

print(f"Area of the rectangle: {rectangle.area()}")
