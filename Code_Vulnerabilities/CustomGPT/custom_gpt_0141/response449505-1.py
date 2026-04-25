
class MaxHeap:
    def __init__(self, arr=[]):
        self.heap = arr
        self.build_max_heap()

    def build_max_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

# Example usage
h1 = MaxHeap([10, 9, 8])
h2 = MaxHeap([7, 6, 5])
combined_heap = MaxHeap(h1.heap + h2.heap)  # Merging by building a new heap
print(combined_heap.heap)  # Should maintain max-heap property
