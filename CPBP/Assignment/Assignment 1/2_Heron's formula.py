# 2. Write a program to calculate the area of a triangle using Heron's formula.

# Taking input for the lengths of the three sides
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculating the semi-perimeter
s = (a + b + c) / 2

# Calculating the area using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Printing the result
print(f"The area of the triangle is: {area:.2f}")