# from abc import ABC, abstractmethod
# import math

# # ABC Abstract  class
# # abstractmethod module used to create abstract method

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def bread(self):
#         print("Pug")
#     def sound(self):
#         print("Bark..")
# create abstract class shape with two abstract methods ;
# area() and perimeter ()
# then implement the child class Rectangle and circle that extend the shape class
# --> the Rectangle should implement a constructor that passes width and height
# area (): width*height
# perimeter () : 2*(width+ height)
# --› the circle should implement a constructor that passes
# radius
# area(): math.pi* radius**2
# perimeter() : 2*math.pi*radius
# -->solve this using function with return
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)

class Circle(Shape):
    def __init__(self, radius, ):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2* math.pi* self.radius

rect = Rectangle(5, 10)
print(f"Rectangle area: {rect.area()}")
print(f"Rectangle perimeter: {rect.perimeter()}")

circle = Circle(7)
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")
