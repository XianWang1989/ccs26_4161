
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, i, n)

def max_heapify(array, i, heap_size):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heap_size and array[left] > array[largest]:
        largest = left
    if right < heap_size and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest, heap_size)

def merge_heaps(h1, h2):
    # Concatenate the heaps
    merged = h1 + h2
    # Build a max heap from the combined list
    build_max_heap(merged)
    return merged

# Example usage
h1 = [10, 5, 3]
h2 = [8, 4, 2]
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # This will result in a valid max heap
