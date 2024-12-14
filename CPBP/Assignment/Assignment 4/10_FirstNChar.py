# 10. Write a program to extract the first n characters of a string. 

def first_n_characters(string, n):
    return string[:n]

input_string = "Hello World!"
n = 5
print("First", n, "characters:", first_n_characters(input_string, n))
