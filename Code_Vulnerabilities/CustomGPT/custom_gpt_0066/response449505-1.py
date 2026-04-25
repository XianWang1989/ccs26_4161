
def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
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

def merge_heaps(h1, h2):
    h1.extend(h2)  # Concatenate heaps
    build_max_heap(h1)  # Rebuild max heap
    return h1

# Example usage:
heap1 = [10, 5, 6, 2]  # Example max heap 1
heap2 = [8, 7, 3]      # Example max heap 2
merged_heap = merge_heaps(heap1, heap2)
print(merged_heap)
