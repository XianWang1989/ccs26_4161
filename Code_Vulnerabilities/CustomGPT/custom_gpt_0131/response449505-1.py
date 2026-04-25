
def build_max_heap(array):
    # Function to build a max heap from an array
    def heapify(array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[left] > array[largest]:
            largest = left

        if right < n and array[right] > array[largest]:
            largest = right

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(array, n, largest)

    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

def merge_heaps(h1, h2):
    # Combine two heaps into a single array
    combined = h1 + h2
    build_max_heap(combined)
    return combined

# Example of using the merge_heaps function:
h1 = [9, 7, 8]  # A max heap
h2 = [10, 6, 5] # Another max heap
merged_heap = merge_heaps(h1, h2)
print("Merged Heap: ", merged_heap)
