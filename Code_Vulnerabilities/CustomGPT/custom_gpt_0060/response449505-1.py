
def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(array, n, i)
    return array

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

def merge_heaps(h1, h2):
    # Step 1: Concatenate the heaps
    merged = h1 + h2
    # Step 2: Build a max heap from the concatenated list
    return build_max_heap(merged)

# Example usage
h1 = [10, 9, 8, 7, 6]  # Example max heap 1
h2 = [15, 12, 11]       # Example max heap 2
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output will be a max heap
