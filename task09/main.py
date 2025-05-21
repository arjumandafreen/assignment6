# 9. Abstract Classes and Methods

# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().


# Create an instance of Rectangle and print the area.


#----------------SOLUTION----------#

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create an instance of Rectangle
rect = Rectangle(5, 10)

# Print the area
print("Area of the rectangle:", rect.area())
