# -------------------------
# 1. Method Overriding (Runtime Polymorphism)
# -------------------------

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()  # Different behavior for same method


# -------------------------
# 2. Duck Typing
# -------------------------

class Pigeon:
    def fly(self):
        print("Pigeon flies")

class Plane:
    def fly(self):
        print("Plane flies in the sky")

def let_it_fly(entity):
    entity.fly()

let_it_fly(Pigeon())  # Doesn't matter the class
let_it_fly(Plane())   # Just needs a fly() method


# -------------------------
# 3. Function Polymorphism using Default Arguments
# -------------------------

def add(a, b=0, c=0):
    return a + b + c

print(add(2))          # 2
print(add(2, 3))       # 5
print(add(2, 3, 4))    # 9


# -------------------------
# 4. Function Polymorphism using *args
# -------------------------

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3))          # 6
print(multiply(2, 3, 4))       # 24
print(multiply(2, 3, 4, 5))    # 120


# -------------------------
# 5. Operator Overloading
# -------------------------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Vector(6, 8)


# -------------------------
# 6. Built-in Function Polymorphism
# -------------------------

print(len("hello"))       # 5
print(len([1, 2, 3, 4]))  # 4
print(len({'a': 1}))      # 1


# -------------------------
# 7. Polymorphism with Inheritance and a Common Interface
# -------------------------

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area method")

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

shapes = [Square(4), Rectangle(2, 5)]
for shape in shapes:
    print("Area:", shape.area())


# -------------------------
# 8. Polymorphic Behavior with isinstance Checks (Not Recommended but Realistic)
# -------------------------

def describe(obj):
    if isinstance(obj, Dog):
        print("It's a dog.")
    elif isinstance(obj, Cat):
        print("It's a cat.")
    else:
        print("Unknown animal.")

describe(Dog())
describe(Cat())
describe(Animal())