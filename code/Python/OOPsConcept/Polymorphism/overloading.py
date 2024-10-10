# class Maths:
#     def add(self,a, b):
#         print(a+b)
#     def add (self, a, b, c):
#         print (a+b+c)
# obj=Maths ()
# obj.add (1,2)
# obj.add (1,2,3)
# Here, the concept of polymorphism cannot be directly implemented in Python. However, using the multiple-dispatch package, we can implement the overloading concept.
# in multiple-dispatch package we are using a decorator known as dispatch decorator.

# decorator in python is a concept that is used to extend a function without any modification
# A decorator is applied using the @decorator_name syntax before the function

from multipledispatch import dispatch

# class Maths:
#     @dispatch(int,int)
#     def add(self,a, b):
#         print(a+b)
#     @dispatch(int,int,int)
#     def add (self, a, b, c):
#         print (a+b+c)
# obj=Maths()
# obj.add (1,2)
# obj.add (1,2,3)

# Create a class datatype_len string,list, dictionary, set, tuple
# without using len function

# class datatype_len:
#     def len(self,a):
#         count = 0
#         for i in a:
#             count += 1
#         print(count)

# obj1=datatype_len()
# obj1.len("hello")
# obj2=datatype_len()
# obj2.len([1, 2, 3, 4])
# obj3=datatype_len()
# obj3.len((1, 2, 3))
# obj4=datatype_len()
# obj4.len({1, 2, 3})
# obj5=datatype_len()
# obj5.len({1: 'a', 2: 'b'})



# class datatype_len:

#     @dispatch(str)
#     def len(self, a):
#         count = 0
#         for i in a:
#             count += 1
#         print("Length of string:", count)

#     @dispatch(list)
#     def len(self, a):
#         count = 0
#         for i in a:
#             count += 1
#         print("Length of list:", count)

#     @dispatch(tuple)
#     def len(self, a):
#         count = 0
#         for i in a:
#             count += 1
#         print("Length of tuple:", count)

#     @dispatch(set)
#     def len(self, a):
#         count = 0
#         for i in a:
#             count += 1
#         print("Length of set:", count)

#     @dispatch(dict)
#     def len(self, a):
#         count = 0
#         for i in a:
#             count += 1
#         print("Length of dictionary:", count)


# obj = datatype_len()
# obj.len("hello")
# obj.len([1, 2, 3, 4])
# obj.len({1: 'a', 2: 'b'})
# obj.len({1, 2, 3})
# obj.len((1, 2, 3))

# create a class datatype
# function outputs
# string reverse
# list output length

class datatype:
    @dispatch(str)
    def output(self,a):
        x = a[::-1]
        print(x)
    @dispatch(list)
    def output(self,a):
        x = len(a)
        print(x)
obj = datatype()
obj.output("hello")
obj.output([1,2,3,4])
