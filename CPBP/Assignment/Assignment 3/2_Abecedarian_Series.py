# Write a program to generate an Abecedarian series. 
# (a series in which elements appears in an alphabetical order)

def abecedarian_series():
    for i in range(ord('a'), ord('z') + 1):
        print(chr(i), end=" ")

# Generate the series
abecedarian_series()
