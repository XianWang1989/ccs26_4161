
def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):  # Start from the last parent node
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
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        max_heapify(arr, n, largest)

def merge_heaps(h1, h2):
    # Concatenate the two heaps
    combined = h1 + h2
    build_max_heap(combined)
    return combined

# Example usage
h1 = [9, 7, 5, 4, 6]  # Example max heap
h2 = [8, 3, 2, 1]     # Example max heap
merged_heap = merge_heaps(h1, h2)
print("Merged Heap:", merged_heap)
