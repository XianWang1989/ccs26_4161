
def build_max_heap(array):
    # Helper function to maintain the max-heap property
    def heapify(index, n):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and array[left] > array[largest]:
            largest = left
        if right < n and array[right] > array[largest]:
            largest = right

        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            heapify(largest, n)

    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(i, n)

def merge_heaps(h1, h2):
    # Combine heaps and rebuild max heap
    combined = h1 + h2
    build_max_heap(combined)
    return combined

# Example usage:
h1 = [10, 5, 3]  # Example max heap
h2 = [8, 7, 2]   # Example max heap
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output the merged max heap
