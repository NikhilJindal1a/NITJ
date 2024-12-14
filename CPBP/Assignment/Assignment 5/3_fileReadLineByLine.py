# 3. Write a program that reads a file line by line and each line read from the file is copied and to
# another file with line numbers specified at the beginning of the line.

source_file = "example.txt"
destination_file = "output.txt"

# Create example.txt
with open(source_file, 'w') as file:
    file.write("Hello World\nPython Programming\nFile Handling Example")

# Copy contents with line numbers
with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
    for line_num, line in enumerate(src, 1):
        dest.write(f"{line_num}: {line}")

print(f"Contents of {source_file} copied to {destination_file} with line numbers.")
