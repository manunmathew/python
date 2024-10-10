class class_name:
    def function_name(self):
        print("Hello World")

obj = class_name() # reference variable
obj.function_name()

# Create a class maths with 4 functions add(), sub(), multiply(), div()
class maths:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def multiply(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)

obj = maths()
obj.add(10,2)
obj.sub(10,2)
obj.multiply(10,2)
obj.div(10,2)
