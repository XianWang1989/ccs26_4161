
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, n, i)

def max_heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, n, largest)

def merge_heaps(h1, h2):
    # Concatenate arrays
    merged_array = h1 + h2
    # Build the max heap
    build_max_heap(merged_array)
    return merged_array

# Example usage
h1 = [10, 7, 6, 5, 4]
h2 = [9, 8, 3, 1]
merged_heap = merge_heaps(h1, h2)
print("Merged Max Heap:", merged_heap)
