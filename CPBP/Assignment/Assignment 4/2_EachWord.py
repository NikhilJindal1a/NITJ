# 2. Write a program to extract each word from a string using a regular expression.

import re

def extract_words(string):
    words = re.findall(r'\b\w+\b', string)
    return words

input_string = "Hello world from Python!"
print("Words:", extract_words(input_string))
