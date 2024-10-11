# Abstraction in Python

**Abstraction** in Python allows us to hide complex implementation details and expose only the essential features of an object. It helps in reducing programming complexity and effort, while focusing on what the object does rather than how it does it.

In Python, **abstraction** is achieved through abstract classes using the `abc` (Abstract Base Class) module. Abstract methods are defined using the `@abstractmethod` decorator.

## Key Concepts

1. **Abstract Base Class (ABC):**
   - Abstract Base Classes provide a blueprint for concrete classes.
   - A class becomes an abstract class by inheriting from `ABC`.
   - You cannot instantiate an abstract class directly.

2. **Abstract Method:**
   - Declared using the `@abstractmethod` decorator.
   - Abstract methods must be implemented by any subclass that inherits from the abstract class.
   - An abstract method has no body in the base class (typically defined with `pass`).

## Example Code

The following example demonstrates abstraction using abstract classes in Python.

```python
from abc import ABC, abstractmethod

# Creating an Abstract Base Class
class BaseClass(ABC):

    # Declaring an abstract method
    @abstractmethod
    def method_1(self):
        pass

# Creating a subclass that inherits from the BaseClass
class DerivedClass(BaseClass):

    # Implementing the abstract method
    def method_1(self):
        print("Implementation of method_1 in DerivedClass")

# Trying to instantiate BaseClass will raise an error
# base_instance = BaseClass()  # This will raise TypeError

# Instantiating DerivedClass and calling the implemented method
derived_instance = DerivedClass()
derived_instance.method_1()  # Output: Implementation of method_1 in DerivedClass
```
## Explanation

### Importing ABC and abstractmethod:
- The `ABC` class and `abstractmethod` decorator are imported from the `abc` module, which is used to define abstract classes.

### Defining BaseClass:
- `BaseClass` inherits from `ABC`, making it an abstract base class.
- Inside `BaseClass`, the method `method_1` is decorated with `@abstractmethod`, indicating that it must be implemented by any subclass.

### Defining DerivedClass:
- `DerivedClass` inherits from `BaseClass`.
- It provides a concrete implementation of the abstract `method_1`.

### Error Handling:
- Attempting to instantiate `BaseClass` directly will raise a `TypeError`, as abstract classes cannot be instantiated.

### Using the Subclass:
- When we instantiate `DerivedClass` and call `method_1`, the implemented logic in the subclass is executed.

## Benefits of Abstraction in Python

- **Simplifies Complex Systems:** By focusing on the essential aspects and hiding implementation details, abstraction makes systems easier to manage and maintain.
- **Promotes Code Reusability:** Abstract classes allow for shared methods across different classes while enforcing a structure for derived classes.
- **Enhances Flexibility:** Subclasses can provide their own implementations for abstract methods, promoting customization and flexibility in design.
