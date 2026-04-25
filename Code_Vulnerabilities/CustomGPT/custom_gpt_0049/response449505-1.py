
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def merge_heaps(h1, h2):
    # Combine both heaps
    combined = h1 + h2
    build_max_heap(combined)
    return combined

# Example usage
h1 = [10, 9, 8]
h2 = [7, 6, 5]
merged_heap = merge_heaps(h1, h2)
print("Merged Heap:", merged_heap)
