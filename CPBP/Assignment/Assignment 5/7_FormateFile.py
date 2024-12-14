# 7. Write a program that writes data to a file in such a way that each character after a full stop is
# capitalized and all the numbers are written in brackets.
source_file = "example.txt"
output_file = "formatted.txt"

# Write to source file
with open(source_file, 'w') as file:
    file.write("hello world. this is a test. python programming is fun.")

# Format and write to output file
with open(source_file, 'r') as file, open(output_file, 'w') as output:
    content = file.read()
    formatted = ""
    capitalize = True

    for char in content:
        if char == '.':
            formatted += '.'
            capitalize = True
        elif capitalize and char.isalpha():
            formatted += char.upper()
            capitalize = False
        else:
            formatted += char

    output.write(formatted)

print(f"Formatted text written to {output_file}.")
