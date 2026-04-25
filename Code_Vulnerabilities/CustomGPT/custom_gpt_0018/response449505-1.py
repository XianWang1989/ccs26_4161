
def max_heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def merge_heaps(h1, h2):
    # Concatenate both heaps and then build a max heap
    merged = h1 + h2
    build_max_heap(merged)
    return merged

# Example usage:
h1 = [10, 5, 6, 2]
h2 = [12, 7, 8]
merged_heap = merge_heaps(h1, h2)
print("Merged Max Heap:", merged_heap)
