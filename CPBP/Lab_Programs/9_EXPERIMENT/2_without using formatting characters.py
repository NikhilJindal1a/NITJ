# WAP to display powers of number without using formatting characters
i=1
while i<=5:
    print(i**1, "\t", i**2, "\t",  i**3, "\t",  i**4)
    i+=1
print()
print()

i=1
while i<=5:
    print("%d\t%d\t%d\t%d"%(i**1, i**2, i**3,  i**4))
    i+=1
print()
print()

i = 1
print("%-4s%-5s%-6s"%('i', 'i**2', 'i**3'))
print()
print()

i = 1
while i<=5:
    print("%-4d%-5d%-6d"%(i, i**2, i**3))
    i+=1
