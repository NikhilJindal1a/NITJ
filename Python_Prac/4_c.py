# c)

# Write a python program to:
# -Accept a list of integers from the user.
# -Rerrange the list such that all the even numbers come before odd numbers, while maintaining the relative orders.

# Accept a list of integers from the user
input_list = input("Enter a list of integers separated by spaces: ").split()

# Convert the input list into integers
input_list = [int(x) for x in input_list]

# Create two separate lists for even and odd numbers
even_numbers = [x for x in input_list if x % 2 == 0]
odd_numbers = [x for x in input_list if x % 2 != 0]

# Concatenate the even and odd lists
result_list = even_numbers + odd_numbers

# Print the rearranged list
print("Rearranged list:", result_list)

# input
# 2 5 8 3 10 7 4

# Output
# [2, 8, 10, 4, 5, 3, 7]





