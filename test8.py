

print("===== isalnum() =====")
s = "abc123"
print(f"{s!r}.isalnum() =>", s.isalnum())

s = "abc 123"
print(f"{s!r}.isalnum() =>", s.isalnum())

print("\n===== isalpha() =====")
s = "HelloWorld"
print(f"{s!r}.isalpha() =>", s.isalpha())

s = "Hello123"
print(f"{s!r}.isalpha() =>", s.isalpha())

print("\n===== isdigit() =====")
s = "123456"
print(f"{s!r}.isdigit() =>", s.isdigit())

s = "123abc"
print(f"{s!r}.isdigit() =>", s.isdigit())

print("\n===== isdecimal() =====")
s = "456"
print(f"{s!r}.isdecimal() =>", s.isdecimal())

s = "Ⅻ"  # Roman numeral 12
print(f"{s!r}.isdecimal() =>", s.isdecimal())

print("\n===== isnumeric() =====")
s = "123"
print(f"{s!r}.isnumeric() =>", s.isnumeric())

s = "²³"  # Superscript digits
print(f"{s!r}.isnumeric() =>", s.isnumeric())

print("\n===== islower() =====")
s = "hello"
print(f"{s!r}.islower() =>", s.islower())

s = "Hello"
print(f"{s!r}.islower() =>", s.islower())

print("\n===== isupper() =====")
s = "HELLO"
print(f"{s!r}.isupper() =>", s.isupper())

s = "Hello"
print(f"{s!r}.isupper() =>", s.isupper())

print("\n===== istitle() =====")
s = "This Is Title Case"
print(f"{s!r}.istitle() =>", s.istitle())

s = "This is not"
print(f"{s!r}.istitle() =>", s.istitle())

print("\n===== isspace() =====")
s = "   \t\n"
print(f"{s!r}.isspace() =>", s.isspace())

s = " a "
print(f"{s!r}.isspace() =>", s.isspace())

print("\n===== isidentifier() =====")
s = "variable1"
print(f"{s!r}.isidentifier() =>", s.isidentifier())

s = "1variable"
print(f"{s!r}.isidentifier() =>", s.isidentifier())

print("\n===== isascii() =====")
s = "Hello123"
print(f"{s!r}.isascii() =>", s.isascii())

s = "你好"
print(f"{s!r}.isascii() =>", s.isascii())
