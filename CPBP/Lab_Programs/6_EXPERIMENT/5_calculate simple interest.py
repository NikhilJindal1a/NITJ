# WAP to calculate simple interest. 
# Suppose the customer is a Senior citizen and is being offered 12% ROI. For all other customers, ROI is 10%.
age = int(input("Enter age of person: "))
principal = float(input("Enter principal amount: "))
time = int(input("Enter time in years: "))
if age>=60:
    r=12
else:
    r=10
si = principal*r*time/100
print("Simple Interest is: ", si)
