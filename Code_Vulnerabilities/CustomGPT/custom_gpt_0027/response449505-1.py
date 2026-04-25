
def build_max_heap(array):
    # Helper function to build a max heap
    n = len(array)
    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)

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

def merge_max_heaps(h1, h2):
    h1.extend(h2)  # Concatenate the heaps
    build_max_heap(h1)  # Rebuild the max heap
    return h1
