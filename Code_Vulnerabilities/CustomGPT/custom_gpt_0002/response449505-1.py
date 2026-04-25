
class MaxHeap:
    def __init__(self, elements=[]):
        self.heap = elements
        self.build_max_heap()

    def build_max_heap(self):
        n = len(self.heap)
        for i in range(n//2 - 1, -1, -1):
            self.max_heapify(i, n)

    def max_heapify(self, i, n):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest, n)

    def merge(self, other_heap):
        combined = self.heap + other_heap.heap
        return MaxHeap(combined)

# Example usage
h1 = MaxHeap([10, 9, 8])
h2 = MaxHeap([7, 6, 5])
merged_heap = h1.merge(h2)

print(merged_heap.heap)  # This will print the merged heap after rebuilding.
