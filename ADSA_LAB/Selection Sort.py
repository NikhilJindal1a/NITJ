# Selection Sort
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Sample input
sample_array = [64, 25, 12, 22, 11]
print("Original array:", sample_array)

# Sorting the array
selection_sort(sample_array)
print("Sorted array:", sample_array)

