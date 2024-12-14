# Function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function to calculate Permutation P(n, r)
def permutation(n, r):
    return factorial(n) // factorial(n - r)

# Function to calculate Combination C(n, r)
def combination(n, r):
    return permutation(n, r) // factorial(r)

# Input: Getting values of n and r from the user
n = int(input("Enter the value of n (total number of objects): "))
r = int(input("Enter the value of r (objects taken at a time): "))

# Call the functions and display the results
p = permutation(n, r)
c = combination(n, r)

print(f"Permutation P({n}, {r}) = {p}")
print(f"Combination C({n}, {r}) = {c}")
