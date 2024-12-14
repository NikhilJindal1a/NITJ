# WAP that creates two sets one of even numbers in the range 1 to 10 and the other as all composite numbers in range 1 to 20
# Demonstrate the use of all(), issuperset(), len() and sum() on the sets.

set1 = {i for i in range(1, 11) if i % 2 == 0 }
print("Set of even numbers: ",set1)

set2 = set()

c = 0
for i in range(2, 21):
    for j in range(2, i):
        if i%j ==0:
            c+=1
    if c!=0:
        set2.add(i)
    c = 0
print("Set of composite numbers: ", set2)

# all() function returns True if all elements are True, else returns False
print("\nDemonstrating use of all() function: ")
print(all(set1))

set1.remove(2)
print("\nRemoving '2' from set1: ", set1)

print("\nDemonstrating use of issuperset() function: ")
print(set2.issuperset(set1))

print("\nDemonstrating use of len() function: ")
print(len(set2))

print("\nDemonstrating use of sum() function: ")
print("Sum of elements of set1: ", sum(set1))
