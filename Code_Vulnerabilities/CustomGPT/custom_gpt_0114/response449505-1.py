
def build_max_heap(arr):
    """ Build a max heap from an unordered array. """
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

def merge_heaps(h1, h2):
    """ Merge two max heaps into one. """
    # Concatenate the two heaps
    new_heap = h1 + h2
    # Build a max heap from the concatenated array
    build_max_heap(new_heap)
    return new_heap

# Example usage
h1 = [10, 5, 4]
h2 = [15, 7, 6]
merged_heap = merge_heaps(h1, h2)
print("Merged Max Heap:", merged_heap)
