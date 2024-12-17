# 1. a) ii.

# 4
# 3 4
# 2 3 4
# 1 2 3 4
# 0 1 2 3 4
# 1 2 3 4
# 2 3 4
# 3 4
# 4
        
# Get the number of rows from the user
n = int(input("Enter the number of rows: "))

#First Half Patten
for i in range(n, -1, -1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print()

#Second Half Patten
for i in range(1, n + 1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print()

