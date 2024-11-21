
a = int(input("Enter a number: "))
arr = []  

for x in range(10):
    arr.append(a * (x + 1))  

print(arr) 

if 35 in arr:
    print("yes 35 is there")
else:
    print("no, 35 is not here")