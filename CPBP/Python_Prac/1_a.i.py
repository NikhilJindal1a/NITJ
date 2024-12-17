# 1. a) 1.

#     A
#    A B
#   A B C
#  A B C D
# A B C D E

#Take the number of rows from user
rows = int(input("Enter the numbers of rows: "))

#Print Patten
for i in range(1, rows + 1):
    # Print Space in row
    print(" " * (rows - i), end="")
    
    #Print Letter in rows
    for j in range(i):
        print(chr(65 + j), end=" ")
        
    #Next line
    print()

