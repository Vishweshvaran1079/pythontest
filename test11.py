# test11.py

# ===========================
# List Operations
# ===========================

# Creating a list
fruits = ['apple', 'banana', 'cherry']
print("Original list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])

# Modifying elements
fruits[1] = 'blueberry'
print("Modified list:", fruits)

# Adding elements
fruits.append('date')
print("After append:", fruits)

fruits.insert(1, 'kiwi')
print("After insert:", fruits)

# Removing elements
fruits.remove('cherry')  # removes by value
print("After remove:", fruits)

popped = fruits.pop()  # removes last element
print("Popped item:", popped)
print("After pop:", fruits)

# Slicing
print("Sliced list [1:3]:", fruits[1:3])

# Looping
print("Looping through list:")
for fruit in fruits:
    print(fruit)

# List comprehension
squared = [x**2 for x in range(5)]
print("List comprehension (squares):", squared)

# List methods
fruits.sort()
print("Sorted list:", fruits)

fruits.reverse()
print("Reversed list:", fruits)

count = fruits.count('apple')
print("Count of 'apple':", count)

# ===========================
# Tuple Operations
# ===========================

# Creating a tuple
person = ('Alice', 30, 'Engineer')
print("\nOriginal tuple:", person)

# Accessing elements
print("Name:", person[0])
print("Age:", person[1])

# Tuple unpacking
name, age, profession = person
print("Unpacked:", name, age, profession)

# Nested tuple
nested = ('Bob', ('Python', 'JavaScript'))
print("Nested tuple:", nested)
print("Second skill:", nested[1][1])

# Slicing
print("Tuple slice [0:2]:", person[0:2])

# Looping
print("Looping through tuple:")
for item in person:
    print(item)

# Tuple methods
nums = (1, 2, 3, 2, 4, 2)
print("Count of 2:", nums.count(2))
print("Index of 4:", nums.index(4))

# Immutability check
try:
    person[1] = 31
except TypeError as e:
    print("Error (tuples are immutable):", e)
