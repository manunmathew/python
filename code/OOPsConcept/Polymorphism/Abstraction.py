from abc import ABC, abstractmethod

# ABC Abstract  class
# abstractmethod module used to create abstract method

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def bread(self):
        print("Pug")
    def sound(self):
        print("Bark..")
