
import heapq

# Function to build a max heap
def build_max_heap(arr):
    # Convert to a min-heap by negating values
    return [-x for x in arr]

# Merging two max heaps
def merge_max_heaps(h1, h2):
    combined = h1 + h2
    return build_max_heap(combined)

# Example usage
h1 = [20, 15, 10, 7, 5]
h2 = [25, 22, 17, 16]

# Build max heaps from the lists
max_heap1 = build_max_heap(h1)
max_heap2 = build_max_heap(h2)

# Merge the max heaps and print the result
merged_heap = merge_max_heaps(max_heap1, max_heap2)
print("Merged Max Heap:", merged_heap)
