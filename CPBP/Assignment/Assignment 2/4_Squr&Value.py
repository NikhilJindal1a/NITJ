# Function to create and return a list of tuples with numbers and their squares
def create_squares_list():
    squares_list = []  
    for i in range(1, 31):  
        squares_list.append((i, i**2))  
    return squares_list

squares = create_squares_list()
print(squares)
