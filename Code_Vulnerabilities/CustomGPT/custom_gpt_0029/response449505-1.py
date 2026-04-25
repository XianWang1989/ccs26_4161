
class MaxHeap:
    def __init__(self, elements=[]):
        self.heap = []
        for element in elements:
            self.insert(element)

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] < self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def build_max_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):
        child = 2 * index + 1
        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child] < self.heap[child + 1]:
                child += 1
            if self.heap[index] < self.heap[child]:
                self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
                index = child
                child = 2 * index + 1
            else:
                break

    def merge(self, other):
        self.heap.extend(other.heap)
        self.build_max_heap()


# Example Usage
h1 = MaxHeap([10, 7, 5])
h2 = MaxHeap([12, 8, 6])
h1.merge(h2)

print(h1.heap)  # This will output the elements of the merged max heap.
