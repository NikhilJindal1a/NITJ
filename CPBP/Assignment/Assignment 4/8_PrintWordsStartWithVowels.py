# 8. Write a program that prints only those words that starts with a vowel.

import re
def words_starting_with_vowel(string):
    words = re.findall(r'\b[aeiouAEIOU]\w*\b', string)
    return words

input_string = "Apple is a fruit and orange is too."
print("Words starting with a vowel:", words_starting_with_vowel(input_string))
