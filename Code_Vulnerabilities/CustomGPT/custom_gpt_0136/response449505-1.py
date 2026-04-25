
def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

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
    # Concatenate the arrays of both heaps
    merged_array = h1 + h2
    build_max_heap(merged_array)
    return merged_array

# Example usage
h1 = [20, 10, 15, 5]  # Example max heap
h2 = [25, 22, 30]     # Another max heap
merged_heap = merge_heaps(h1, h2)
print("Merged Max Heap:", merged_heap)
