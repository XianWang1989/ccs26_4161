
import heapq

def build_max_heap(arr):
    # Builds a max heap from a list
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))

def heapify(arr, i, size):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, size)

def merge_heaps(h1, h2):
    # Combine two heaps
    combined = h1 + h2
    build_max_heap(combined)
    return combined

# Example usage
h1 = [10, 5, 6, 2]  # max heap
h2 = [15, 7, 9]     # max heap

merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output will be a valid max heap
