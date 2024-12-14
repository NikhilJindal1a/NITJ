# Write a program that counts the occurrences of a character in a string. Do not use built in functions. 

def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

# Take input from user
string = input("Enter a string: ")
char = input("Enter a character to count: ")

# Display result
print(f"The character '{char}' appears {count_occurrences(string, char)} times in the string.")
