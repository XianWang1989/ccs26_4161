
def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, n, i)

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def merge_heaps(h1, h2):
    # Concatenate the two arrays
    new_heap = h1 + h2
    # Build a max heap from the concatenated array
    build_max_heap(new_heap)
    return new_heap

# Example usage
h1 = [10, 8, 9]
h2 = [7, 5, 6]
merged_heap = merge_heaps(h1, h2)
print("Merged max heap:", merged_heap)  # Output should still satisfy heap properties
