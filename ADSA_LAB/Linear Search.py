# Linear Search 

def linear_search(arr, target):
    # Traverse the array element by element
    for i in range(len(arr)):
        # Check if the current element matches the target
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if the element is not in the array

# Sample input
sample_array = [10, 20, 30, 40, 50]
target_value = 30

# Searching for the target value
result = linear_search(sample_array, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}.")
else:
    print(f"Element {target_value} not found.")
