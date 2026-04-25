
import heapq

def build_max_heap(arr):
    # Convert to max-heap using heapq (min-heap by default)
    return [-x for x in arr]

def merge_max_heaps(h1, h2):
    # Combine the heaps and re-build the max heap
    combined = h1 + h2
    return build_max_heap(combined)

# Example usage
h1 = [20, 15, 10, 5, 7]
h2 = [25, 30, 40]
h1 = build_max_heap(h1)  # Convert to max-heap
h2 = build_max_heap(h2)  # Convert to max-heap

merged_heap = merge_max_heaps(h1, h2)
print(merged_heap)
