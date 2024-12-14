# Write a program to get a single string from two given strings separated by a space and swap the first two characters of each string.

def swap_first_two(str1, str2):
    if len(str1) >= 2 and len(str2) >= 2:
        return str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
    else:
        return "Both strings should have at least 2 characters."

# Take input from user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Display result
print("Result after swapping:", swap_first_two(str1, str2))
