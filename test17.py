# 1. Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 2. Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 3. Sum of natural numbers
def sum_natural(n):
    if n <= 0:
        return 0
    return n + sum_natural(n - 1)

# 4. Power (x^n)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

# 5. GCD
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 6. Reverse string
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

# 7. Palindrome check
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# 8. Binary Search
def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

# 9. Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

# 10. Flatten nested list
def flatten_list(nested):
    if not nested:
        return []
    if isinstance(nested[0], list):
        return flatten_list(nested[0]) + flatten_list(nested[1:])
    return [nested[0]] + flatten_list(nested[1:])

# ----------------------
# Test calls for output
# ----------------------

print("1. Factorial of 5:", factorial(5))
print("2. 6th Fibonacci number:", fibonacci(6))
print("3. Sum of first 10 natural numbers:", sum_natural(10))
print("4. 2 raised to power 5:", power(2, 5))
print("5. GCD of 48 and 18:", gcd(48, 18))
print("6. Reverse of 'recursion':", reverse_string("recursion"))
print("7. Is 'madam' a palindrome?:", is_palindrome("madam"))
print("8. Binary search for 7 in [1,2,3,4,5,6,7,8,9]:", binary_search([1,2,3,4,5,6,7,8,9], 7))

print("\n9. Tower of Hanoi with 3 disks:")
tower_of_hanoi(3, 'A', 'B', 'C')

print("\n10. Flatten nested list [1, [2, [3, 4], 5], 6]:")
print(flatten_list([1, [2, [3, 4], 5], 6]))
