
def build_max_heap(arr):
    # Build a max heap from the array
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
    return arr

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
    # Merge two heaps by concatenating, then building a max heap
    merged = h1 + h2
    return build_max_heap(merged)

# Example usage
h1 = [10, 5, 6, 2]    # Max heap
h2 = [9, 3, 4]         # Max heap
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output should be a valid max heap
