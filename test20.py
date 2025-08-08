
"""
Abstraction in Python - Code Examples
Exploring the use of abstract classes, methods, and their real-world application.
"""

from abc import ABC, abstractmethod

# Example 1: Basic Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Example 2: Abstract Class with Concrete Method
class Shape(ABC):
    def describe(self):
        return "This is a shape"

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Example 3: Preventing Instantiation
try:
    a = Animal()
except TypeError as e:
    print(f"Error: {e}")

# Example 4: Interface-style Abstract Class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Bike(Vehicle):
    def start(self):
        return "Bike started"

    def stop(self):
        return "Bike stopped"

# Example 5: Partial Abstraction (some methods implemented)
class Appliance(ABC):
    def plug_in(self):
        return "Plugged in"

    @abstractmethod
    def operate(self):
        pass

class WashingMachine(Appliance):
    def operate(self):
        return "Washing clothes"

# Example 6: Using Abstract Classes in Real Application

class DataProcessor(ABC):
    @abstractmethod
    def read_data(self, source):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def write_data(self, destination):
        pass

class CSVDataProcessor(DataProcessor):
    def read_data(self, source):
        print(f"Reading data from {source}")

    def process_data(self):
        print("Processing CSV data")

    def write_data(self, destination):
        print(f"Writing data to {destination}")

if __name__ == "__main__":
    # Demo of basic abstraction
    dog = Dog()
    print("Dog sound:", dog.make_sound())

    cat = Cat()
    print("Cat sound:", cat.make_sound())

    # Demo of shape abstraction
    c = Circle(5)
    print("Circle area:", c.area())

    # Demo of interface-style abstraction
    b = Bike()
    print(b.start())
    print(b.stop())

    # Demo of partial abstraction
    wm = WashingMachine()
    print(wm.plug_in())
    print(wm.operate())

    # Demo of real application
    processor = CSVDataProcessor()
    processor.read_data("data.csv")
    processor.process_data()
    processor.write_data("output.csv")
