
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def build_max_heap(self):
        start_index = (len(self.heap) // 2) - 1
        for i in range(start_index, -1, -1):
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
    merged_heap = MaxHeap()
    merged_heap.heap = h1.heap + h2.heap
    merged_heap.build_max_heap()
    return merged_heap

# Example usage
h1 = MaxHeap()
h1.insert(10)
h1.insert(20)
h1.insert(30)

h2 = MaxHeap()
h2.insert(5)
h2.insert(15)

merged = merge_heaps(h1, h2)
print(merged.heap)  # Output should be a valid max heap
