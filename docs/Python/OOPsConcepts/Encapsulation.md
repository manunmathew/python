# Encapsulation in Python

Encapsulation in Python is used to define the **visibility** and **accessibility** of attributes and methods within a class. It helps in restricting direct access to some components of an object, which is a fundamental aspect of object-oriented programming.

## Types of Access Modifiers

In Python, encapsulation is typically classified into three types of access modifiers:

### 1. Public Access Modifier
- Attributes and methods that are public can be accessed both **within** and **outside** the class.
- **By default**, all attributes and methods are public.

```python
class Example:
    def __init__(self):
        self.public_var = "I am public"

    def public_method(self):
        return "This is a public method"

obj = Example()
print(obj.public_var)  # Accessible
print(obj.public_method())  # Accessible
```

### 2. Private Access Modifier

Private members are accessible only within the class where they are defined.
In Python, private members are declared by prefixing the attribute or method name with two underscores (`__`).
Name mangling is used to access private members from outside the class (although it's not recommended).

```python
class Example:
    def __init__(self):
        self.__private_var = "I am private"

    def __private_method(self):
        return "This is a private method"

    def access_private(self):
        return self.__private_method()

obj = Example()
# print(obj.__private_var)  # Raises AttributeError
# print(obj.__private_method())  # Raises AttributeError
print(obj.access_private())  # Accessible through a public method
```
### 3. Protected Access Modifier

Protected members are accessible within the class and its subclasses.
They are defined with a single underscore (`_`), which is a convention rather than strict enforcement.

```python
class Example:
    def __init__(self):
        self._protected_var = "I am protected"

    def _protected_method(self):
        return "This is a protected method"

class SubExample(Example):
    def access_protected(self):
        return self._protected_var

obj = SubExample()
print(obj.access_protected())  # Accessible within the subclass
```

### Name mangling
The name mangling process helps to access the class variables from outside the class. The class variables can be accessed by adding _classname to it
```python

class ExampleClass:
    def __init__(self):
        self.__private_var = "I am private!"

# Create an instance
example = ExampleClass()

# Accessing the variable directly will cause an error
# print(example.__private_var)  # This raises an AttributeError

# Name mangling allows access with the class name prefix
print(example._ExampleClass__private_var)  # Output: I am private!


```
### Summary
- **Public**: Accessible from anywhere.
- **Private**: Accessible only within the class (name mangling can be used to access).
- **Protected**: Accessible within the class and its subclasses (not enforced, but follows convention).

