# main.py

import mymodule

# Arithmetic
print("Add:", mymodule.add(10, 5))
print("Subtract:", mymodule.subtract(10, 5))
print("Multiply:", mymodule.multiply(10, 5))
print("Divide:", mymodule.divide(10, 5))
print("Divide by zero:", mymodule.divide(10, 0))

# String ops
print("Reversed string:", mymodule.reverse_string("hello world"))
print("Capitalized:", mymodule.capitalize_words("hello from python"))

# List ops
print("No duplicates:", mymodule.remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print("Sorted list:", mymodule.sort_list([5, 3, 1, 4, 2]))
print("Reverse sorted list:", mymodule.sort_list([5, 3, 1, 4, 2], reverse=True))

# Using the class
g = mymodule.Greeter("Vishwesh")
print(g.greet())
print(g.yell())
