# Write a program that takes the user's name and pan card number as input. Validate the 
# information using isX function and print the details.

def validate_details(name, pan_number):
    if name.isalpha() and pan_number.isalnum() and len(pan_number) == 10:
        return f"Name: {name}, PAN Card Number: {pan_number}"
    else:
        return "Invalid details entered."

# Take input from user
name = input("Enter your name: ")
pan_number = input("Enter your PAN card number: ")

# Display result
print(validate_details(name, pan_number))
