import heapq

# Since heapq is a min-heap by default, we store negative values for max-heap behavior
def build_max_heap(arr1, arr2):
    merged = [-x for x in arr1 + arr2]
    heapq.heapify(merged)  # O(n)
    return [-x for x in merged]

h1 = [50, 30, 20]
h2 = [45, 25, 10]
H = build_max_heap(h1, h2)
print(H)  # Outputs a valid max-heap
