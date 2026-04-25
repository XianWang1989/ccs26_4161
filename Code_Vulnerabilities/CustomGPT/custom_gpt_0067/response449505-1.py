
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, n, i)

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def merge_heaps(h1, h2):
    # Concatenate the arrays from both heaps
    merged = h1 + h2
    # Build a new max heap
    build_max_heap(merged)
    return merged

# Example Usage
h1 = [10, 5, 6, 2]  # Max Heap representation
h2 = [9, 3, 8, 1]
merged_heap = merge_heaps(h1, h2)
print(merged_heap)
