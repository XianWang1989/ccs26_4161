
def build_max_heap(nums):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

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
    # Assuming h1 and h2 are arrays representing max heaps.
    merged = h1 + h2
    build_max_heap(merged)
    return merged

# Example usage
h1 = [10, 5, 3]  # max heap
h2 = [8, 4, 2]   # max heap

merged_heap = merge_heaps(h1, h2)
print("Merged Max Heap:", merged_heap)
