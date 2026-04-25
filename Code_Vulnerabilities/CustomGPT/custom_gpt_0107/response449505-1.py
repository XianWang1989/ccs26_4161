
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

def merge_heaps(h1, h2):
    # Combine the arrays
    combined = h1 + h2
    build_max_heap(combined)
    return combined

# Example usage:
h1 = [10, 5, 6, 2]  # A max heap
h2 = [9, 3, 8]      # Another max heap
merged_heap = merge_heaps(h1, h2)
print(merged_heap)   # This will print the merged max heap
