
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Logic to maintain the max heap property
        pass # Implement this based on your heap structure

    def build_max_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):
        # Logic to maintain the max heap property
        pass # Implement this based on your heap structure

def merge_heaps(h1, h2):
    # Create a new MaxHeap
    merged_heap = MaxHeap()

    # Merge both heaps into one
    for value in h1.heap:
        merged_heap.insert(value)
    for value in h2.heap:
        merged_heap.insert(value)

    return merged_heap

# Example Usage
h1 = MaxHeap()
h2 = MaxHeap()
# Assume we populate the heaps with values here

merged = merge_heaps(h1, h2)
