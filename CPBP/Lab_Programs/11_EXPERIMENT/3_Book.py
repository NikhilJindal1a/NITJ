# Write a menu driven program that keeps record of books and journals available in a library. 
# class book
# attributes of constructor - title, author name, price of book
# two functions - read and display()
# use logic that if you have list of books in a list, then you have a choice for read() and display() for that particular book.


class Book():
    def __init__(self,):
        self.title = ""
        self.author = ""
        self.price = ""
    def read(self):
        print()
        self.title = input("Enter title of book: ")
        self.author = input("Enter name of author of book: ")
        self.price = input("Enter price of book: ")
    def display(self):
        print("-----------")
        print("Title of book: ", self.title)
        print("Author of book: ", self.author)
        print("Price of book: ", self.price)
        print("-----------")

list_of_books = []
while True:
    print()
    print("***********************************************************")
    ch = input("Enter your choice:\n1. Press 1 to enter a new book into the system.\n2. Press 2 to display all records.\n3. Press 3 to search book by title and print its details\n4. Press 4 to search book by author and print its details\n5. Press anything else to exit\nEnter your choice: ")
    if int(ch) == 1:
        obj = Book()
        obj.read()
        list_of_books.append(obj)
    elif int(ch) == 2:
        for i in list_of_books:
            i.display()
            print()
    elif int(ch) == 3:
        pat = input("Enter the search keyword in title: ")
        for i in list_of_books:
            if pat.lower() in i.title.lower():
                i.display()
    elif int(ch) == 4:
        pat = input("Enter the search keyword in author name: ")
        for i in list_of_books:
            if pat.lower() in i.author.lower():
                i.display()
    else:
        print("Invalid choice! Exiting the program")
        break
    
