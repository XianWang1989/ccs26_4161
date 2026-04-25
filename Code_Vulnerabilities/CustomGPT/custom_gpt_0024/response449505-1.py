
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def build_max_heap(self):
        n = len(self.heap)
        for i in range(n//2 - 1, -1, -1):
            self._heapify_down(i)

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
    merged = MaxHeap()
    merged.heap = h1.heap + h2.heap
    merged.build_max_heap()
    return merged

# Example usage
h1 = MaxHeap()
h1.insert(10)
h1.insert(5)
h1.insert(20)

h2 = MaxHeap()
h2.insert(30)
h2.insert(25)

merged_heap = merge_heaps(h1, h2)
print(merged_heap.heap)  # Should print a valid max heap
