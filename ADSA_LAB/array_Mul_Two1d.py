arrSize = int(input("Enter the Size of array: "))

arr1 = []

print("Enter the elements of first array: ")
for i in range(arrSize):
    element1 = int(input())
    arr1.append(element1)
    
arr2 =[]
print("Enter the elements of Second array: ")
for i in range(arrSize):
    element2 = int(input())
    arr2.append(element2)
    
mulArray = []
for i in range(arrSize):
    mulArray.append(arr1[i]*arr2[i])

print("Multiplication of two 1D array is: ", mulArray)        
