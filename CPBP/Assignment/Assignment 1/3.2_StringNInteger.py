
""" 3.2 Given a string s = "1234" and an integer n = 5678,
concatenate them as a single string and then convert the result back to an integer.
What is the final integer value? """
s = "1234"
n = 5678

# Convert the integer to a string and concatenate
concatenated_string = s + str(n)

# Convert the concatenated string back to an integer
final_integer = int(concatenated_string)

# Print the final integer value
print(f"The final integer value is: {final_integer}")
