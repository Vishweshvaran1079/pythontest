a = 5
b = 3
c = 8

result = ((a + b * c) // (c - b) + (a % b)) * (a ^ b) - (a << 1) + (~c)
print("Mixed Expression Result:", result)

# Bonus: Function-Based
def evaluate(a, b, c):
    return ((a + b * c) // (c - b) + (a % b)) * (a ^ b) - (a << 1) + (~c)

print("Function Result:", evaluate(5, 3, 8))
