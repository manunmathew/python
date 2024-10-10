
# class A:
#     def fun1(self):
#         print("class A body")
# class B(A):
#     def fun1(self):
#         print("class B body")
# obj = B()
# obj.fun1()


# # multiple inheritance
# class A:
#     def fun1(self):
#         print("class A body")

# class B:
#     def fun2(self):
#         print("class B body")
# class C(A,B):
#     def fun1(self):
#         print("class C body")
#     def fun2(self):
#         print("class C body")
# obj = C()
# obj.fun1()
# obj.fun2()
# # multilevel inheritance
# class A:
#     def fun1(self):
#         print("class A body")

# class B(A):
#     def fun1(self):
#         print("class B body")
# class C(B):
#     def fun1(self):
#         print("class C body")

# obj = C()
# obj.fun1()

# Create  a class shape with method area that returns 0(zero)
# Create rectangle class that derive from shape and override  area method to return the area of rectangle (length X width) length and width are pass through rectangular constructor
# create a class circle derives from shape and overrides area to return the area of circle


class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.1416 * (self.radius ** 2)

rect = Rectangle(5, 3)
print(f"Area of rectangle: {rect.area()}")

circle = Circle(4)
print(f"Area of circle: {circle.area()}")
