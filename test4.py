


#  Basic Shift + OR Example
a = 0b1010  # 10 in binary
b = 0b0101  # 5 in binary

result = (a << 2) | (b >> 1)

print("a << 2 =", bin(a << 2))    # 0b101000
print("b >> 1 =", bin(b >> 1))    # 0b0010
print("Result (OR):", bin(result))
print("Result (decimal):", result)

print("\n---\n")

#  Bigger Combo Expression
x = 13      # 0b1101
y = 7       # 0b0111
z = 4       # 0b0100

combo = ((x << 1) | (y >> 1)) | (z << 2)

print("x << 1 =", bin(x << 1))     # 0b11010
print("y >> 1 =", bin(y >> 1))     # 0b0011
print("z << 2 =", bin(z << 2))     # 0b10000
print("Final Result (binary):", bin(combo))
print("Final Result (decimal):", combo)

print("\n---\n")

#  Function-Based Complex Expression
def bitwise_shift_or(a, b, c):
    return ((a << 2) | (b >> 1)) | (c << 1)

print("Bitwise Combo Result:", bitwise_shift_or(5, 10, 3))

print("\n---\n")

#  Mega Expression (All Together)
a = 0b1100   # 12
b = 0b0011   # 3
c = 0b1010   # 10

result = ((a >> 1) | (b << 2)) | ((c >> 1) << 1)

print("Final Complex Bitwise OR:", bin(result))
print("Decimal:", result)

print("\n=== Arithmetic + Boolean + Bitwise Expression Tests ===\n")

#  Expression Test Suite 1: Arithmetic + Boolean + Nesting
a = 10
b = 5
c = 3
d = 2

result = ((a + b) * c - d ** 2) / (b % c + 1) + (a // c) * (b - d)
print("Arithmetic Result:", result)

#  Expression Test Suite 2: Bitwise Madness
x = 0b1101  # 13
y = 0b1011  # 11
z = 0b1000  # 8

bitwise_result = ((x & y) | (~z)) ^ (x << 2) & (y >> 1)
print("Bitwise Result (binary):", bin(bitwise_result))
print("Bitwise Result (decimal):", bitwise_result)


