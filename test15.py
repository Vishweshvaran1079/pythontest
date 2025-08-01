# typecasting_examples_full.py

# 1. Integer to Float
x = 10
y = float(x)
print("Integer to Float:", y)  # Output: 10.0

# 2. Float to Integer
a = 15.7
b = int(a)
print("Float to Integer:", b)  # Output: 15

# 3. String to Integer
s = "123"
n = int(s)
print("String to Integer:", n + 1)  # Output: 124

# 4. String to Float
s2 = "3.14"
f = float(s2)
print("String to Float:", f + 1)  # Output: 4.14

# 5. Integer to String
num = 42
str_num = str(num)
print("Integer to String:", str_num + " is a number")  # Output: 42 is a number

# 6. Float to String
pi = 3.14159
pi_str = str(pi)
print("Float to String:", pi_str + " is pi")  # Output: 3.14159 is pi

# 7. Boolean to Integer
flag = True
int_flag = int(flag)
print("Boolean to Integer:", int_flag)  # Output: 1

# 8. Integer to Boolean
zero = 0
bool_zero = bool(zero)
print("Integer to Boolean (0):", bool_zero)  # Output: False

# 9. List to Tuple
lst = [1, 2, 3]
tpl = tuple(lst)
print("List to Tuple:", tpl)  # Output: (1, 2, 3)

# 10. Tuple to List
t = (4, 5, 6)
l = list(t)
print("Tuple to List:", l)  # Output: [4, 5, 6]

# 11. List to Set
list_with_duplicates = [1, 2, 2, 3, 4, 4]
unique_set = set(list_with_duplicates)
print("List to Set:", unique_set)  # Output: {1, 2, 3, 4}

# 12. Set to List
num_set = {5, 6, 7}
num_list = list(num_set)
print("Set to List:", num_list)  # Output: [5, 6, 7] (order may vary)

# 13. String to List
word = "hello"
char_list = list(word)
print("String to List:", char_list)  # Output: ['h', 'e', 'l', 'l', 'o']

# 14. List to String
chars = ['H', 'i']
joined = ''.join(chars)
print("List to String:", joined)  # Output: Hi

# 15. Int to Binary / Hex / Octal (String)
num = 25
print("Int to Binary:", bin(num))   # Output: 0b11001
print("Int to Hex:", hex(num))      # Output: 0x19
print("Int to Octal:", oct(num))    # Output: 0o31

# 16. Binary / Hex String to Int
binary_str = "0b1101"
hex_str = "0x1F"
print("Binary to Int:", int(binary_str, 2))  # Output: 13
print("Hex to Int:", int(hex_str, 16))      # Output: 31

# 17. Float to Complex
flt = 5.5
comp = complex(flt)
print("Float to Complex:", comp)  # Output: (5.5+0j)

# 18. String to Boolean
str_val = "True"
bool_val = bool(str_val)
print("String to Boolean:", bool_val)  # Output: True (non-empty string is True)

# 19. Dict to List of Keys
my_dict = {"a": 1, "b": 2}
keys_list = list(my_dict)
print("Dict to List of Keys:", keys_list)  # Output: ['a', 'b']

# 20. Dict to List of Items
items_list = list(my_dict.items())
print("Dict to List of Items:", items_list)  # Output: [('a', 1), ('b', 2)]
