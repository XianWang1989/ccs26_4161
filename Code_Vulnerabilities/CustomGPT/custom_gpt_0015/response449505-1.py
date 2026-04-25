
class MaxHeap:
    def __init__(self, elements=[]):
        self.heap = []
        for element in elements:
            self.insert(element)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def merge(self, other_heap):
        new_elements = self.heap + other_heap.heap
        return MaxHeap(new_elements)

# Example usage
h1 = MaxHeap([10, 7, 5, 4, 3])
h2 = MaxHeap([12, 8, 6, 2, 1])
merged_heap = h1.merge(h2)
print(merged_heap.heap)  # Outputs a merged max heap
