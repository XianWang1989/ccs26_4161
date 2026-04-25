
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
    # Combine the two heaps
    combined = h1 + h2
    # Build a max heap from the combined array
    build_max_heap(combined)
    return combined

# Example usage
h1 = [10, 9, 8]
h2 = [7, 6, 5]
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output: A valid max heap
