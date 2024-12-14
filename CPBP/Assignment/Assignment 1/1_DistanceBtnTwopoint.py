# 1. Write a program to calculate the distance between two points.

# Taking input for the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Taking input for the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculating the distance using the distance formula
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Printing the result
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")