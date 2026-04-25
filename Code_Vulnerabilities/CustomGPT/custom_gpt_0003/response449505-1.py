
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

def heapify(array, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if left child is larger than root
    if left_child < n and array[left_child] > array[largest]:
        largest = left_child

    # Check if right child is larger than largest so far
    if right_child < n and array[right_child] > array[largest]:
        largest = right_child

    # If largest is not root
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def merge_heaps(h1, h2):
    # Combine both heaps into a new array
    combined = h1 + h2
    # Build a max heap from the combined array
    build_max_heap(combined)
    return combined

# Example usage
h1 = [10, 5, 6, 2]  # Max Heap
h2 = [9, 3, 7]      # Max Heap

merged_heap = merge_heaps(h1, h2)
print("Merged Heap:", merged_heap)  # Output will be a max heap
