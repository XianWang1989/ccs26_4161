
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, i, n)

def max_heapify(array, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest, n)

def merge_heaps(h1, h2):
    # Concatenate the two heaps
    merged = h1 + h2
    # Build the max heap from the concatenated array
    build_max_heap(merged)
    return merged

# Example usage:
h1 = [10, 5, 6, 2]  # Max heap
h2 = [12, 7, 9]     # Max heap
merged_heap = merge_heaps(h1, h2)
print(merged_heap)   # Output may vary: valid max heap is created
