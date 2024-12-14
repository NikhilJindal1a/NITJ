# Function to calculate the sum of cubes of individual digits
def cubesum(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10
    return total

# Function to check if a number is an Armstrong number
def isArmstrong(n):
    return n == cubesum(n)

# Function to print all Armstrong numbers in a range
def PrintArmstrong(start, end):
    for i in range(start, end + 1):
        if isArmstrong(i):
            print(i)

# Example Usage
num = int(input("Enter a number to check if it's an Armstrong number: "))
if isArmstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# Printing Armstrong numbers in a range
print("Armstrong numbers between 1 and 999:")
PrintArmstrong(1, 999)
