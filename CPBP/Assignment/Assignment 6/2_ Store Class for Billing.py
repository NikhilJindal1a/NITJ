# 2. Write a program that has a class store which keeps a record of code 
# and price of each product. Display a menu of all products to the user and prompt him to enter 
# the quantity of each item required. Generate a bill and display the total amount.

class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, code, price):
        self.products[code] = price

    def generate_bill(self):
        total = 0
        print("Available Products:")
        for code, price in self.products.items():
            print(f"Code: {code}, Price: {price}")
        print()
        for code in self.products:
            quantity = int(input(f"Enter quantity for product {code}: "))
            total += self.products[code] * quantity
        print(f"\nTotal Bill Amount: {total}")

# Example usage
store = Store()
store.add_product("P001", 50)
store.add_product("P002", 100)
store.add_product("P003", 150)
store.generate_bill()
