
class MaxHeap:
    def __init__(self, data=[]):
        self.heap = []
        for item in data:
            self.insert(item)

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
    combined = h1.heap + h2.heap
    new_heap = MaxHeap(combined)
    new_heap.build_max_heap()
    return new_heap

# Example usage
h1 = MaxHeap([10, 3, 5])
h2 = MaxHeap([8, 7, 15])
merged_heap = merge_heaps(h1, h2)
print(merged_heap.heap)  # Output: Should represent a valid max heap
