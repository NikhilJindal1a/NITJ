# 4. Write a program to print the last word of the string. 
def last_word(string):
    words = string.split()
    return words[-1] if words else ""

# Input
input_string = "Hello world from Python!"
print("Last word:", last_word(input_string))
