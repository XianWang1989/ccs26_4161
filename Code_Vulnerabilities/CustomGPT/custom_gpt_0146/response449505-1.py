
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def build_max_heap(self, array):
        self.heap = array
        start = (len(array) // 2) - 1
        for i in range(start, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):
        size = len(self.heap)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

def merge_heaps(h1, h2):
    merged = MaxHeap()
    merged.build_max_heap(h1.heap + h2.heap)
    return merged

# Example usage
heap1 = MaxHeap()
heap1.insert(10)
heap1.insert(5)
heap1.insert(6)
heap1.insert(3)

heap2 = MaxHeap()
heap2.insert(9)
heap2.insert(4)
heap2.insert(2)

merged_heap = merge_heaps(heap1, heap2)
print(merged_heap.heap)  # Output will represent a valid max heap
