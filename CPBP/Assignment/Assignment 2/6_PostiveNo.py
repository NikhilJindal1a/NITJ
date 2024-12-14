# Enter a positive integer

def get_pos_int():
    while True: 
        num = int(input("Enter a +ve integer: "))
        if num > 0:
            print(f"Thank you! You entered a +Ve integer: {num}")
            break  # Exit the loop if the input is valid
        else:
            print("Invalid input. Please enter a +ve integer.")

# Call the function
get_pos_int()

