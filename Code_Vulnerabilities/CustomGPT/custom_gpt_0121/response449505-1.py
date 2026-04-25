
import heapq

def build_max_heap(arr):
    # Convert array to a max heap
    return [-x for x in arr]

def merge_heaps(h1, h2):
    # Concatenate the heaps
    merged = h1 + h2
    # Build max heap
    max_heap = build_max_heap(merged)
    # Transform into a proper max heap (negative values)
    return [-x for x in max_heap]

# Example Usage
h1 = [10, 5, 3]  # Representation of a max heap
h2 = [8, 4, 2]   # Representation of a max heap

merged_heap = merge_heaps(h1, h2)
print(merged_heap)  # Should maintain max heap properties
