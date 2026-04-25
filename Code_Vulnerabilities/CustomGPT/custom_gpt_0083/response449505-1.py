
def merge_heaps(h1, h2):
    # Convert heaps into a combined array representation
    combined = h1 + h2

    # Function to build max heap from the array
    def build_max_heap(array):
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            max_heapify(array, n, i)

    # Function to maintain the max heap property
    def max_heapify(array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[left] > array[largest]:
            largest = left
        if right < n and array[right] > array[largest]:
            largest = right

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            max_heapify(array, n, largest)

    build_max_heap(combined)
    return combined
