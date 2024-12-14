# 3.1 Write a program to calculate the bill amount for an item given its quantity sold, value, discount, and tax

# Taking inputs from the user
quantity = float(input("Enter the quantity sold: "))
value = float(input("Enter the value of the item: "))
discount = float(input("Enter the discount percentage: "))
tax = float(input("Enter the tax percentage: "))

# Calculating the total value before discount
total_value = quantity * value

# Calculating the discount amount
discount_amount = (discount / 100) * total_value

# Calculating the total value after discount
value_after_discount = total_value - discount_amount

# Calculating the tax amount
tax_amount = (tax / 100) * value_after_discount

# Calculating the final bill amount
final_bill_amount = value_after_discount + tax_amount

# Printing the final bill amount
print(f"The final bill amount is: RS {final_bill_amount:.2f}")
