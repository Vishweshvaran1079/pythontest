# Dictionary Basics and Operations

# 1. Creating dictionaries
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}

# 2. Accessing values
print("Name:", person["name"])  # Direct access
print("City:", person.get("city"))  # Using get() method

# 3. Adding or updating items
person["age"] = 31  # Update
person["email"] = "alice@example.com"  # Add
print("Updated person:", person)

# 4. Removing items
del person["city"]  # Using del
email = person.pop("email", None)  # Using pop() safely
print("After deletion:", person)
print("Popped email:", email)

# 5. Checking existence of keys
print("Has 'age'? ->", "age" in person)
print("Has 'city'? ->", "city" in person)

# 6. Iterating through dictionary
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key} => {value}")

# 7. Dictionary methods
keys = person.keys()
values = person.values()
items = person.items()
print("Keys:", list(keys))
print("Values:", list(values))
print("Items:", list(items))

# 8. Copying a dictionary
copy_person = person.copy()
print("Copy:", copy_person)

# 9. Clearing all items
copy_person.clear()
print("Cleared copy:", copy_person)

# 10. Nested dictionaries
employees = {
    "emp1": {"name": "Bob", "position": "Manager"},
    "emp2": {"name": "Sara", "position": "Engineer"},
}
print("Nested dictionary:", employees)
print("emp1 name:", employees["emp1"]["name"])
