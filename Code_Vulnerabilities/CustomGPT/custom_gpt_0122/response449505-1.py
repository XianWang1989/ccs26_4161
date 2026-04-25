
def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
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

def merge(h1, h2):
    # Combine both heaps
    combined = h1 + h2
    # Build a max heap from the combined array
    build_max_heap(combined)
    return combined

# Example usage
h1 = [10, 9, 8, 7]
h2 = [15, 13, 12]

merged_heap = merge(h1, h2)
print(merged_heap)  # Output should be a valid max heap
