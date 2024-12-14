# 6. Write a simple basic calculator program in python.Direction:

# Displaying the menu to the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Taking user input for the operation
operation = input("Enter the number of the operation (1/2/3/4): ")

# Taking user input for the numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing the operation based on user choice
if operation == '1':
    result = num1 + num2
    print(f"The result of addition is: {result}")

elif operation == '2':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")

elif operation == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")

elif operation == '4':
    # Handling division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid input! Please select a valid operation.")
