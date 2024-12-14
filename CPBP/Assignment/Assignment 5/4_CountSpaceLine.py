# 4. Write a program that counts the number of tabs, spaces and newline characters in a file.
file_name = "example.txt"

with open(file_name, 'r') as file:
    content = file.read()

tabs = content.count('\t')
spaces = content.count(' ')
newlines = content.count('\n')

print(f"Tabs: {tabs}")
print(f"Spaces: {spaces}")
print(f"Newlines: {newlines}")

