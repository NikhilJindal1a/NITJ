""" 4. Given two variables, a = 7 and b = 3,
write a Python code snippet to swap their values without using a temporary variable.
What will be the values of a and b after the swap? """

# Given variables
a = 7
b = 3

# Swapping the values without using a temp var
a = a + b
b = a - b
a = a - b

# Printing the values after the swap
print(f"Value of a after swap: {a}")
print(f"Value of b after swap: {b}")
