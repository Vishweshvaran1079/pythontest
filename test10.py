# test10.py — All common string operations in Python

# 1. String Creation
s = "Hello, World!"
multiline = """This
is a
multiline string."""

# 2. Indexing & Slicing
s = "Python"
print(s[0])       # 'P'
print(s[-1])      # 'n'
print(s[1:4])     # 'yth'
print(s[:3])      # 'Pyt'
print(s[::2])     # 'Pto'

# 3. Length
print(len("Python"))  # 6

# 4. Iteration
for char in "abc":
    print(char)

# 5. Membership Test
print("Py" in "Python")     # True
print("x" not in "Python")  # True

# 6. Concatenation & Repetition
print("Py" + "thon")       # 'Python'
print("Go! " * 3)          # 'Go! Go! Go! '

# 7. Case Conversion
s = "hello WORLD"
print(s.lower())       # 'hello world'
print(s.upper())       # 'HELLO WORLD'
print(s.capitalize())  # 'Hello world'
print(s.title())       # 'Hello World'
print(s.swapcase())    # 'HELLO world'

# 8. Strip / Trim
s = "   hello  \n"
print(s.strip())       # 'hello'
print(s.lstrip())      # 'hello  \n'
print(s.rstrip())      # '   hello'

# 9. Search and Replace
s = "hello world"
print(s.find("world"))         # 6
print(s.replace("world", "Python"))  # 'hello Python'

# 10. Split & Join
s = "a,b,c"
print(s.split(","))            # ['a', 'b', 'c']
print(" ".join(['one', 'two'])) # 'one two'

# 11. Start / End Check
s = "Python programming"
print(s.startswith("Py"))     # True
print(s.endswith("ing"))      # True

# 12. Character Checks
s = "abc123"
print(s.isalpha())       # False
print(s.isdigit())       # False
print(s.isalnum())       # True
print("  ".isspace())    # True
print("Hello".istitle()) # True

# 13. String Formatting
name = "Alice"
print("Hello, %s" % name)  # Old style
print("Hello, {}".format("Bob"))  # format()
print(f"{name} is {30} years old")  # f-string

# 14. Encoding / Decoding
s = "hello"
b = s.encode("utf-8")
print(b)                  # bytes
print(b.decode("utf-8"))  # string

# 15. Reverse
s = "Python"
print(s[::-1])  # 'nohtyP'

# 16. Count
s = "banana"
print(s.count("a"))  # 3

# 17. String Comparison
print("a" == "A")                    # False
print("a".lower() == "A".lower())   # True

# 18. Raw Strings
path = r"C:\Users\name"
print(path)

# 19. Splitlines
s = "line1\nline2\nline3"
print(s.splitlines())

# 20. Translation
s = "abc"
table = str.maketrans("abc", "123")
print(s.translate(table))  # '123'
