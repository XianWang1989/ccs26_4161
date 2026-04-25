
def merge_heaps(h1, h2):
    # Concatenate the two heaps
    merged_heap = h1 + h2  # Assuming h1 and h2 are list representations

    # Build a max heap from the combined list
    return build_max_heap(merged_heap)

def build_max_heap(array):
    n = len(array)
    # Start from the last non-leaf node and heapify down
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    return array

def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

# Example usage
h1 = [10, 8, 7, 6]
h2 = [15, 14, 13]
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output should be a valid max heap
