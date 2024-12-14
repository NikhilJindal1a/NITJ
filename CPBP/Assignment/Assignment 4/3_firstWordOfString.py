# 3. Write a program to print the first word of the string. 
def first_word(string):
    words = string.split()
    return words[0] if words else ""


input_string = "Hello world from Python!"
print("First word:", first_word(input_string))
