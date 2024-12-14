# 5. Write a program that reads data from the file and calculates the percentage of vowels and
# consonants in the file.
file_name = "example.txt"

vowels = consonants = total_chars = 0

with open(file_name, 'r') as file:
    content = file.read().lower()
    for char in content:
        if char.isalpha():
            total_chars += 1
            if char in 'aeiou':
                vowels += 1
            else:
                consonants += 1

print(f"Percentage of vowels: {(vowels / total_chars) * 100:.2f}%")
print(f"Percentage of consonants: {(consonants / total_chars) * 100:.2f}%")
