# 1. Write a program to extract each character from a string using a regular expression.

import re

def extract_characters(string):
    characters = re.findall(r'.', string)
    return characters

input_string = "Hello"
print("Characters:", extract_characters(input_string))
