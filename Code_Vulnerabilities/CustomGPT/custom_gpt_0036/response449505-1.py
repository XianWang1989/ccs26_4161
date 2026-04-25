
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
    # Convert heaps to arrays
    merged = h1 + h2
    build_max_heap(merged)
    return merged

# Example usage
h1 = [10, 9, 8, 7, 6]
h2 = [12, 11, 5]

merged_heap = merge_heaps(h1, h2)
print(merged_heap)
