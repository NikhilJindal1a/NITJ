# Write a function to get the first half of half of a specified string of even length. 

def first_half(string):
    if len(string) % 2 == 0:
        return string[:len(string)//2]
    else:
        return "The string length is not even."

# Take input from user
input_string = input("Enter a string of even length: ")

# Display result
print("First half of the string:", first_half(input_string))
