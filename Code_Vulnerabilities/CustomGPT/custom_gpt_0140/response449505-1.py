
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
    # Step 1: Combine the heaps into one list
    combined = h1 + h2
    # Step 2: Build a max heap from the combined list
    build_max_heap(combined)
    return combined

# Example usage
h1 = [10, 5, 3]  # Max heap represented as an array
h2 = [8, 6]      # Another max heap
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output will be a valid max heap
