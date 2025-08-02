# mymodule.py

# Arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Division by zero error"

# String operations
def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

# List operations
def remove_duplicates(lst):
    return list(set(lst))

def sort_list(lst, reverse=False):
    return sorted(lst, reverse=reverse)

# A sample class
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

    def yell(self):
        return f"{self.name.upper()}!!!"
