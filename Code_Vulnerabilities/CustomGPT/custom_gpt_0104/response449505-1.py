
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

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

def merge_heaps(h1, h2):
    # Concatenate both heaps
    merged_heap = h1 + h2
    # Build max heap from the merged list
    build_max_heap(merged_heap)
    return merged_heap

# Example usage:
h1 = [9, 7, 8]  # Represents a max heap
h2 = [5, 6, 4]  # Represents another max heap

merged_h = merge_heaps(h1, h2)
print("Merged Max Heap:", merged_h)
