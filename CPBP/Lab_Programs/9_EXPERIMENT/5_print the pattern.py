# WAP to print the pattern
for i in range(1, 7):
    ch = 'A'
    print()
    for j in range(1, i+1):
        print(ch, end="")
        ch = chr(ord(ch)+1)
