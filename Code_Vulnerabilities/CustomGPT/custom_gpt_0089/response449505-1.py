
import heapq

def build_max_heap(arr):
    # Create a max heap using heapq by inverting the values
    return [-x for x in arr]

def merge_heaps(h1, h2):
    # Concatenate both heaps
    combined = h1 + h2
    # Build a max heap
    return build_max_heap(combined)

# Example heaps
h1 = [10, 7, 5, 3, 2]
h2 = [8, 6, 4]

# Merging heaps
merged_heap = merge_heaps(h1, h2)
print("Merged Heap:", merged_heap)
