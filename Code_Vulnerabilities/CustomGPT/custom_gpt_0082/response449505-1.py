
def merge_heaps(h1, h2):
    # Combine the arrays from both heaps
    combined = h1 + h2
    # Build a max heap from the combined list
    return build_max_heap(combined)

def build_max_heap(array):
    n = len(array)
    # Start from the last non-leaf node and sift down
    for i in range(n // 2 - 1, -1, -1):
        sift_down(array, i, n)

def sift_down(array, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # Swap
        sift_down(array, largest, n)

# Example usage:
h1 = [10, 5, 3]  # Max heap
h2 = [8, 7, 4]   # Another max heap
merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Output will be a valid max heap
