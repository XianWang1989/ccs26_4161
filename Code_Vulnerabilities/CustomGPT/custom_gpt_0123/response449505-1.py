
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def build_max_heap(self):
        n = len(self.heap)
        for i in range(n//2 - 1, -1, -1):
            self._heapify_down(i, n)

    def _heapify_down(self, index, n):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest, n)

def merge_heaps(h1, h2):
    new_heap = MaxHeap()
    new_heap.heap = h1.heap + h2.heap  # Concatenate both heaps
    new_heap.build_max_heap()  # Rebuild the max heap
    return new_heap

# Example usage
h1 = MaxHeap()
h1.insert(10)
h1.insert(5)
h1.insert(3)

h2 = MaxHeap()
h2.insert(12)
h2.insert(6)
h2.insert(1)

merged_heap = merge_heaps(h1, h2)
print(merged_heap.heap)  # This will output the array representation of the merged heap
