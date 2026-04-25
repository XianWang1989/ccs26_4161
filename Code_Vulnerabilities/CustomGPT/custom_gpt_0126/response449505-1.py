
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    def build_max_heap(self):
        start = (len(self.heap) - 2) // 2
        for index in range(start, -1, -1):
            self._heapify_down(index)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

def merge_heaps(h1, h2):
    merged_heap = MaxHeap()
    merged_heap.heap = h1.heap + h2.heap  # Concatenate heaps
    merged_heap.build_max_heap()  # Rebuild max heap
    return merged_heap

# Example Usage
h1 = MaxHeap()
h1.insert(10)
h1.insert(20)
h1.insert(30)

h2 = MaxHeap()
h2.insert(5)
h2.insert(15)

merged = merge_heaps(h1, h2)
print(merged.heap)  # Output should be a valid max heap
