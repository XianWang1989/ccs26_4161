
def build_max_heap(array):
    n = len(array)
    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)

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

def merge_heaps(h1, h2):
    # Concatenate the two heaps
    combined = h1 + h2
    # Build a max heap from the combined array
    build_max_heap(combined)
    return combined

# Example usage
h1 = [10, 7, 5, 3, 2]
h2 = [15, 12, 11]
merged_heap = merge_heaps(h1, h2)
print("Merged Max Heap:", merged_heap)
