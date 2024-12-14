# 6. Write a program to print only the first two characters of every word.

def first_two_chars_each_word(string):
    return [word[:2] for word in string.split()]

input_string = "Hello world from Python"
print("First two characters of each word:", first_two_chars_each_word(input_string))
