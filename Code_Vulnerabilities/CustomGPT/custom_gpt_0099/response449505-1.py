
def max_heapify(heap, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and heap[left] > heap[largest]:
        largest = left
    if right < heap_size and heap[right] > heap[largest]:
        largest = right

    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        max_heapify(heap, largest, heap_size)

def build_max_heap(heap):
    heap_size = len(heap)
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(heap, i, heap_size)

def merge_heaps(h1, h2):
    merged = h1 + h2
    build_max_heap(merged)
    return merged

# Example Usage:
h1 = [10, 7, 9]
h2 = [15, 12, 6]
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output should be a valid max heap
