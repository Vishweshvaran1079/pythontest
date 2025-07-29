# File: test12.py

# ----------------------------
# 1. Creating Sets
# ----------------------------

# Using curly braces
my_set = {1, 2, 3}
print("Initial my_set:", my_set)

# Using set() function
another_set = set([4, 5, 6])
print("another_set:", another_set)

# Creating an empty set
empty_set = set()
print("empty_set:", empty_set)

# ----------------------------
# 2. Adding Elements
# ----------------------------
my_set.add(4)
print("After adding 4:", my_set)

# ----------------------------
# 3. Removing Elements
# ----------------------------

# remove() will raise KeyError if element not present
my_set.remove(2)
print("After removing 2:", my_set)

# discard() won’t raise an error if element not present
my_set.discard(10)
print("After discarding 10 (non-existent):", my_set)

# ----------------------------
# 4. Set Operations
# ----------------------------

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
print("Union:", set_a | set_b)  # or set_a.union(set_b)

# Intersection
print("Intersection:", set_a & set_b)  # or set_a.intersection(set_b)

# Difference
print("Difference (A - B):", set_a - set_b)

# Symmetric Difference
print("Symmetric Difference:", set_a ^ set_b)

# ----------------------------
# 5. Membership Test
# ----------------------------
print("Is 3 in set_a?", 3 in set_a)
print("Is 10 in set_b?", 10 in set_b)

# ----------------------------
# 6. Set Comparison
# ----------------------------
set_c = {1, 2}
print("Is set_c a subset of set_a?", set_c.issubset(set_a))
print("Is set_a a superset of set_c?", set_a.issuperset(set_c))
print("Are set_a and set_b disjoint?", set_a.isdisjoint(set_b))

# ----------------------------
# 7. Copying and Clearing
# ----------------------------
copy_set = set_a.copy()
print("Copy of set_a:", copy_set)

set_a.clear()
print("After clearing set_a:", set_a)
