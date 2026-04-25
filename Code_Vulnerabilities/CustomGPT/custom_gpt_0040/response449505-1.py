
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

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def merge_heaps(h1, h2):
    combined = h1 + h2
    build_max_heap(combined)
    return combined

# Example Usage
h1 = [9, 7, 6, 5]
h2 = [8, 4, 3]
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # The output will be a valid max heap
