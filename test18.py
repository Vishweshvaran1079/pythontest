# =============================
# INHERITANCE EXAMPLES
# =============================

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Multi-level Inheritance
class Puppy(Dog):
    def is_puppy(self):
        return True

# Multiple Inheritance
class Walker:
    def walk(self):
        return "Walking..."

class PetDog(Dog, Walker):
    def play(self):
        return "Playing fetch."

# Usage
a = Animal("GenericAnimal")
d = Dog("Rex")
c = Cat("Whiskers")
p = Puppy("Tiny")
pd = PetDog("Bolt")

print(a.speak())        # GenericAnimal makes a sound.
print(d.speak())        # Rex barks.
print(c.speak())        # Whiskers meows.
print(p.speak())        # Tiny barks.
print(p.is_puppy())     # True
print(pd.speak())       # Bolt barks.
print(pd.walk())        # Walking...
print(pd.play())        # Playing fetch.

# =============================
# INT METHODS AND OPERATIONS
# =============================

i = 123

print(i.bit_length())       # Returns number of bits to represent the int
print(i.to_bytes(2, 'big')) # Converts int to bytes
print(int.from_bytes(b'\x00{', 'big'))  # Converts bytes to int

# Integer formatting
print(bin(i))               # Binary: 0b1111011
print(oct(i))               # Octal: 0o173
print(hex(i))               # Hexadecimal: 0x7b

# Type conversions
print(str(i))               # '123'
print(float(i))             # 123.0

# =============================
# STRING METHODS
# =============================

s = "  Hello, World!  "

print(s.strip())            # Remove whitespace from both ends
print(s.lower())            # hello, world!
print(s.upper())            # HELLO, WORLD!
print(s.title())            # Hello, World!
print(s.startswith("  He")) # True
print(s.endswith("!  "))    # True

print(s.replace("World", "Python"))  # Replace substrings
print(s.split(","))                 # Split by comma
print(s.find("World"))              # Index of substring
print(s.index("Hello"))             # Like find(), but raises error if not found
print(s.count("l"))                 # Count occurrences

# Joining and formatting
parts = ['One', 'Two', 'Three']
joined = "-".join(parts)
print(joined)              # One-Two-Three

formatted = f"Number: {i}, String: {s.strip()}"
print(formatted)           # Number: 123, String: Hello, World!

# Checking content
print("123".isdigit())     # True
print("abc".isalpha())     # True
print("abc123".isalnum())  # True
print("abc def".isspace()) # False
print("  ".isspace())      # True

# Encoding
print("hello".encode())    # b'hello'

