
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, n, i)

def max_heapify(array, n, i):
    largest = i
    left = 2 * i + 1  # Left child
    right = 2 * i + 2 # Right child

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, n, largest)

def merge_heaps(h1, h2):
    # Step 1: Concatenate the two heaps
    merged = h1 + h2
    # Step 2: Build a max heap from the merged array
    build_max_heap(merged)
    return merged

# Example usage:
h1 = [10, 7, 9, 5, 2]
h2 = [15, 8, 12, 3]
merged_heap = merge_heaps(h1, h2)

print(merged_heap)  # The output will be a max-heap
