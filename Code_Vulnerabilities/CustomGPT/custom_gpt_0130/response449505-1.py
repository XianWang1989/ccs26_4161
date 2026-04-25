
def build_max_heap(array):
    # Implement the heapify process
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
    # Combine the two heaps
    combined = h1 + h2
    build_max_heap(combined)
    return combined

# Example usage
h1 = [20, 15, 10]
h2 = [30, 25, 5]
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output will maintain max heap property
