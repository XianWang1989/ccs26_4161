
def build_max_heap.array(arr):
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
    # Concatenate both heaps
    combined = h1 + h2
    build_max_heap(combined)
    return combined

# Example usage
h1 = [10, 5, 3]  # Example max heap
h2 = [8, 7, 4]
merged_heap = merge_heaps(h1, h2)
print(merged_heap)
