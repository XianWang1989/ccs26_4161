
def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def merge_max_heaps(h1, h2):
    # Combine both heaps into a single array
    combined = h1 + h2
    # Build a max heap from the combined array
    build_max_heap(combined)
    return combined

# Example Usage

h1 = [10, 9, 8, 7]  # Example max heap
h2 = [15, 14, 12]  # Another max heap

merged_heap = merge_max_heaps(h1, h2)
print("Merged Max Heap:", merged_heap)
