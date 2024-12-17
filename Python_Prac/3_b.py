# b)

"""WAP that writes a data to a file in such a way that each character after 
a full stop is caplitalized and all the numbers are written in brackets."""


#Take text input from the user
text = input("Enter your text: ")

#Open a file in write mode
with open("output.txt", "w") as file:
    processed_text = ""
    
    #Flag to track if the next character should be capitalized
    capitalize_next = True

    #Loop through each character in the text
    for i in range(len(text)):
        char = text[i]
        
        #Capitalize the first character after a full stop or at the start
        if capitalize_next and char.isalpha():
            processed_text += char.upper()
            capitalize_next = False  # Reset flag after capitalizing
        
        #If the character is a full stop, set the flag to capitalize the next letter
        elif char == '.':
            processed_text += char
            capitalize_next = True
        
        #Enclose numbers in brackets
        elif char.isdigit():
            processed_text += f"({char})"
        
        #If not a number or after a full stop, just add the character as is
        else:
            processed_text += char
    
    #Write the processed text to the file
    file.write(processed_text)

print("Processed text has been written to 'output.txt'.")



# sample input
# my name is nikhil. i love coding. 503 is my favorite number.

# Output
# My name is nikhil. I love coding. (5)(0)(3) Is my favorite number.