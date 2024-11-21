def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Sample input
sample_array = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", sample_array)

# Sorting the array
bubble_sort(sample_array)
print("Sorted array:", sample_array)
