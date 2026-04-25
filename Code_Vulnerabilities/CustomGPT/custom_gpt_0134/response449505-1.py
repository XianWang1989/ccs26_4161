
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
    # Concatenate the heaps
    merged = h1 + h2
    # Build a max heap from the merged array
    build_max_heap(merged)
    return merged

# Example usage
h1 = [10, 9, 8, 7]
h2 = [15, 14, 13]
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output will be a valid max heap
