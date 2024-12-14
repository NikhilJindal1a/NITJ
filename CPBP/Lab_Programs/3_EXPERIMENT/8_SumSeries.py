# WAP to sum the series numbers - 1 + 1/2 + ... + 1/n using for loop
n = int(input("Enter the number: "))
s = 0
for i in range(1, n+1):
    s += (1/i)
print("Sum of series is: ", s)
