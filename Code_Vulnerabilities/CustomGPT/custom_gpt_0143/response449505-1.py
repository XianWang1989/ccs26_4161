
class MaxHeap:
    def __init__(self, elements=None):
        self.heap = elements or []
        self.build_max_heap()

    def build_max_heap(self):
        n = len(self.heap)
        for i in range(n//2 - 1, -1, -1):
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

    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] > self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

def merge_heaps(h1, h2):
    # Create a new max heap from the elements of both heaps
    new_heap = MaxHeap(h1.heap + h2.heap)
    return new_heap
