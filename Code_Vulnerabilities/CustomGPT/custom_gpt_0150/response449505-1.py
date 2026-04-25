
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def build_max_heap(self):
        start_idx = (len(self.heap) // 2) - 1
        for idx in range(start_idx, -1, -1):
            self._heapify_down(idx)

    def _heapify_down(self, index):
        child = index * 2 + 1
        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child] < self.heap[child + 1]:
                child += 1
            if self.heap[index] < self.heap[child]:
                self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
                index = child
                child = index * 2 + 1
            else:
                break

def merge_heaps(h1, h2):
    merged_heap = MaxHeap()
    merged_heap.heap = h1.heap + h2.heap  # Concatenate arrays
    merged_heap.build_max_heap()  # Rebuild the max heap
    return merged_heap
