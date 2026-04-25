
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, n, i)
    return array

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
    combined = h1 + h2  # Concatenate arrays
    return build_max_heap(combined)

# Example Usage:
h1 = [9, 5, 6, 2]  # Example max heap 1
h2 = [8, 7, 3]     # Example max heap 2
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Should print a valid max heap
