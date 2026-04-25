
import heapq

def build_max_heap(arr):
    # Convert the input list to a valid max heap (in-place)
    for i in range(len(arr)//2 - 1, -1, -1):
        max_heapify(arr, i, len(arr))

def max_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)

def merge_heaps(h1, h2):
    merged = h1 + h2  # Concatenate the heaps
    build_max_heap(merged)
    return merged

# Example Usage
h1 = [10, 7, 8, 5]
h2 = [15, 13, 16]
H = merge_heaps(h1, h2)
print("Merged Heap:", H)
