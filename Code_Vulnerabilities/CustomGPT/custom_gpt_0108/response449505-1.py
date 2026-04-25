
def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        max_heapify(arr, i, n)

def max_heapify(arr, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)

def merge_heaps(h1, h2):
    # Concatenate and build max heap
    merged_heap = h1 + h2
    build_max_heap(merged_heap)
    return merged_heap

# Example usage
h1 = [9, 7, 8, 6]
h2 = [10, 5, 4, 2]
merged = merge_heaps(h1, h2)
print(merged)  # Should print a combined max heap
