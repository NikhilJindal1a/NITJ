# Array Updation
import array
arr = array.array('i', [1,2,3,1,2,5])
for i in range(0,6):
    print(arr[i], end = " ")
print("\nAfter updation")
arr[2]=6
for i in range(0,6):
    print(arr[i], end=" ")

# Create empty tuple: 
tuple1 = ()
print(tuple1)
