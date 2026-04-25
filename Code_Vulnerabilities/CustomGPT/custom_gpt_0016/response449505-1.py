
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, n, i)

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
    # Combine the two heaps
    merged = h1 + h2
    # Create a new max heap from the combined list
    build_max_heap(merged)
    return merged

# Example usage:
h1 = [10, 8, 9]  # a sample max heap
h2 = [5, 7, 6]   # another sample max heap
new_heap = merge_heaps(h1, h2)
print(new_heap)  # This will print the merged max heap
