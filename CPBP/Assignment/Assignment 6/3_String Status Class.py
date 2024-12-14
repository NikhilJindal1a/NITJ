# 3. Write a class that stores a string and 
# all its status details such as number of uppercase 
# characters, vowels, consonants, spaces etc.

class StringStatus:
    def __init__(self, input_string):
        self.string = input_string

    def calculate_status(self):
        vowels = "aeiouAEIOU"
        self.uppercase = sum(1 for char in self.string if char.isupper())
        self.vowel_count = sum(1 for char in self.string if char in vowels)
        self.consonants = sum(1 for char in self.string if char.isalpha() and char not in vowels)
        self.spaces = self.string.count(' ')

    def display_status(self):
        self.calculate_status()
        print(f"String: {self.string}")
        print(f"Uppercase Letters: {self.uppercase}")
        print(f"Vowels: {self.vowel_count}")
        print(f"Consonants: {self.consonants}")
        print(f"Spaces: {self.spaces}")

# Example usage
status = StringStatus("Hello World!")
status.display_status()
