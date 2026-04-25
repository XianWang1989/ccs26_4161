
def build_max_heap(array):
    # Helper function to maintain the max heap property
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(array)    
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

def merge_heaps(h1, h2):
    # Combine arrays and build a max heap from the result
    combined = h1 + h2
    build_max_heap(combined)
    return combined

# Example usage
h1 = [10, 7, 3]  # Example max heap
h2 = [9, 5, 2]
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output will be a valid max heap
