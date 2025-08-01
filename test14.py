# Functions and Their Operations

# 1. Basic function definition and call
def greet():
    print("Hello, world!")

greet()

# 2. Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# 3. Function with return value
def add(a, b):
    return a + b

result = add(3, 5)
print("Addition result:", result)

# 4. Default parameter values
def greet_with_default(name="Guest"):
    print(f"Welcome, {name}!")

greet_with_default()
greet_with_default("Bob")

# 5. Keyword arguments
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person(age=25, name="Sara", city="Boston")

# 6. Variable-length arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

print("Sum:", sum_all(1, 2, 3, 4, 5))

# 7. Keyword variable-length arguments (**kwargs)
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="Tom", age=40, job="Engineer")

# 8. Lambda function
multiply = lambda x, y: x * y
print("Multiplication:", multiply(4, 5))

# 9. Function returning multiple values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

stats = get_stats([10, 20, 30, 40])
print("Min, Max, Avg:", stats)

# 10. Nested functions
def outer():
    def inner():
        print("Inside inner function")
    print("Inside outer function")
    inner()

outer()

# 11. Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# 12. Pass statement (empty function)
def todo_function():
    pass
