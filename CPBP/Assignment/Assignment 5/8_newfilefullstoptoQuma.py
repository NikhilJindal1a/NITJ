# #8. Write a program that reads and copies the contents in another file. While copying replace all
# full stops with commas.

source_file = "example.txt"
destination_file = "output.txt"

# Write to source file
with open(source_file, 'w') as file:
    file.write("Hello World. This is a test. File handling in Python.")

# Replace full stops with commas
with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
    content = src.read()
    content = content.replace('.', ',')
    dest.write(content)

print(f"Contents of {source_file} copied to {destination_file} with full stops replaced by commas.")
