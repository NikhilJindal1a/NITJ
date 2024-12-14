# 9. Write a program that uses a regular expression to match strings which starts with an upper-case character followed by a digit and a ‘- ‘.

import re
def match_uppercase_digit_dash(string):
    if re.match(r'^[A-Z]\d- ', string):
        return "Match found"
    else:
        return "No match"

input_string = "A1- Hello"
print(match_uppercase_digit_dash(input_string))
