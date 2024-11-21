# Binary Search 

def binary_search(arr, target):
    # Define the start and end indices
    start = 0
    end = len(arr) - 1

    # Loop until the range is valid
    while start <= end:
        mid = (start + end) // 2  # Find the middle index

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        # If the target is smaller, adjust the end index
        elif arr[mid] > target:
            end = mid - 1
        # If the target is larger, adjust the start index
        else:
            start = mid + 1

    return -1  # Return -1 if the target is not found

# Sample input
sample_array = [10, 20, 30, 40, 50]
target_value = 30

# Searching for the target value
result = binary_search(sample_array, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}.")
else:
    print(f"Element {target_value} not found.")
