
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
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
    merged = h1 + h2  # concatenate the two heaps
    build_max_heap(merged)
    return merged

# Example usage:
h1 = [10, 5, 6]
h2 = [15, 7, 8]
result = merge_heaps(h1, h2)
print(result)  # This will give you a valid max heap
