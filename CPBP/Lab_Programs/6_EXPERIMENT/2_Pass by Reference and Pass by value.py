# Pass by Reference and Pass by value

def square(item_list):
#     Returns the square of the number
    squares = []
    for i in item_list:
        squares.append(i**2)
    return squares

# Pass by reference
num = [1,2,3,4,5]
obj = square(num)
print(obj)

# Pass by value
obj = square([1,2,3,4,5])
print(obj)
