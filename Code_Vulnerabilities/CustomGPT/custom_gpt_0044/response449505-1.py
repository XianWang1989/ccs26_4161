
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

def build_max_heap(arr):
    n = len(arr) // 2 - 1
    for i in range(n, -1, -1):
        max_heapify(arr, len(arr), i)

def merge_heaps(h1, h2):
    merged = h1 + h2
    build_max_heap(merged)
    return merged

# Example of usage
h1 = [10, 5, 3, 2, 1]  # Example max heap
h2 = [9, 6, 4]         # Another max heap
merged_heap = merge_heaps(h1, h2)
print(merged_heap)     # Output: A valid max heap.
