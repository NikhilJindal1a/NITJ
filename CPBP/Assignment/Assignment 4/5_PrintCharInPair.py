# 5. Write the program to print the characters in pairs.
def character_pairs(string):
    return [string[i:i+2] for i in range(0, len(string), 2)]

input_string = "abcdef"
print("Character pairs:", character_pairs(input_string))
