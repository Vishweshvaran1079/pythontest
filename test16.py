# exception_examples_extended.py

# Example 1: ZeroDivisionError
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {result}")
    finally:
        print("Finished divide()\n")


# Example 2: ValueError on int conversion
def convert_input(s):
    try:
        number = int(s)
    except ValueError:
        print(f"Invalid integer: '{s}'")
    else:
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    finally:
        print("Finished convert_input()\n")


# Example 3: IndexError with lists
def get_element(lst, index):
    try:
        print("Element:", lst[index])
    except IndexError:
        print("Index out of range.")
    finally:
        print("Finished get_element()\n")


# Example 4: KeyError with dictionaries
def get_dict_value(d, key):
    try:
        value = d[key]
    except KeyError:
        print(f"Key '{key}' not found in dictionary.")
    else:
        print(f"Value: {value}")
    finally:
        print("Finished get_dict_value()\n")


# Example 5: FileNotFoundError
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    finally:
        print("Finished read_file()\n")


# Example 6: Custom Exception
class NegativeNumberError(Exception):
    pass

def square_root(n):
    try:
        if n < 0:
            raise NegativeNumberError("Negative number provided.")
        print(f"Square root: {n ** 0.5}")
    except NegativeNumberError as e:
        print("Custom Exception:", e)
    finally:
        print("Finished square_root()\n")


# Example 7: Multiple exceptions
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Can't divide by zero.")
    except TypeError:
        print("Only numbers allowed.")
    else:
        print("Safe divide result:", result)
    finally:
        print("Finished safe_divide()\n")


# Example 8: Raising exceptions manually
def validate_age(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        print(f"Age is valid: {age}")
    except ValueError as e:
        print("Error:", e)
    finally:
        print("Finished validate_age()\n")


# Example 9: Loop with exception handling
def process_numbers(nums):
    for i in nums:
        try:
            print(f"Reciprocal of {i} is {1 / i}")
        except ZeroDivisionError:
            print("Can't divide by zero.")
        finally:
            print("Loop iteration complete.\n")


# Example 10: Nested try-except
def nested_example():
    try:
        print("Outer try block")
        try:
            print("Inner try block")
            x = 1 / 0
        except ZeroDivisionError:
            print("Caught inside inner block.")
        else:
            print("Inner else.")
    except:
        print("Caught in outer block.")
    finally:
        print("Finished nested_example()\n")


# ==== FUNCTION CALLS (Test cases) ====

divide(10, 2)
divide(5, 0)

convert_input("100")
convert_input("abc")

get_element([1, 2, 3], 1)
get_element([1, 2, 3], 5)

get_dict_value({"name": "Alice"}, "name")
get_dict_value({"name": "Alice"}, "age")

read_file("file_does_not_exist.txt")

square_root(25)
square_root(-9)

safe_divide(10, 0)
safe_divide(10, "five")

validate_age(30)
validate_age(-5)

process_numbers([2, 0, 5])

nested_example()
