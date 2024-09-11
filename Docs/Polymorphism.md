# Python Polymorphism
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

An example of a Python function that can be used on different objects is the len() function.

## method overloading

Here, the concept of polymorphism cannot be directly implemented in Python. However, using the multiple-dispatch package, we can implement the overloading concept.
in multiple-dispatch package we are using a decorator known as dispatch decorator.

decorator in python is a concept that is used to extend a function without any modification
A decorator is applied using the @decorator_name syntax before the function

## method overriding
Same function name with same argument
Required inheritance

```python
class A:
    def fun1(self):
        print("class A body")
class B(A):
    def fun1(self):
        print("class B body")
obj = B()
obj.fun1()
```

```python
class A:
    def fun1(self):
        print("class A body")

class B:
    def fun2(self):
        print("class B body")
class C(A,B):
    def fun1(self):
        print("class C body")
    def fun2(self):
        print("class C body")
obj = c()
obj.fun1()
obj.fun2()
```
```python
class A:
    def fun1(self):
        print("class A body")

class B(A):
    def fun1(self):
        print("class B body")
class C(B):
    def fun1(self):
        print("class C body")

obj = C()
obj.fun1()
```
