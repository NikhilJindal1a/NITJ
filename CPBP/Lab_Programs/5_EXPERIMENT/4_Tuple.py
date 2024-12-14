# Create empty tuple: 
tuple1 = ()
print(tuple1)

# Create tuple using string: 
tuple1 = ('Hello', 'Sam')
print(tuple1)

# Create tuple using list: 
list1 = ['Hello', 'Sam']
print(tuple(list1))

# Create a tuple using built-in function: 
tuple1 = tuple('Sam')
print(tuple1)

# Creating a tuple with mixed datatypes
tuple1 = (5, 'aiojdio', 7, 'JFidsof')
print(tuple1)

# Nested tuples

t1 = (1,2,3)
t2 = ('a', 'b', 'c')
t3 = (t1, t2)
print(t3)

# Program to demonstrate use of nested tuples

Toppers = (("arav", 97, "B.Sc."), ("raghav", 87, "BCA"))
for i in Toppers:
    print(i)
