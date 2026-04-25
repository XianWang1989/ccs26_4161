
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

def merge_heaps(h1, h2):
    # Concatenate the two heaps
    merged = h1 + h2
    # Build a max heap from the merged array
    build_max_heap(merged)
    return merged

# Example usage
h1 = [10, 5, 3, 2]  # Max heap 1
h2 = [12, 7, 6]     # Max heap 2
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output should be a valid max heap
