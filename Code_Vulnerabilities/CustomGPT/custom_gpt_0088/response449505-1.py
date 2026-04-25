
class MaxHeap:
    def __init__(self, elements=[]):
        self.heap = elements
        self.build_max_heap()

    def build_max_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest)

def merge_heaps(h1, h2):
    combined = h1.heap + h2.heap
    return MaxHeap(combined)

# Example usage
h1 = MaxHeap([10, 7, 9])
h2 = MaxHeap([15, 8, 12])
merged_heap = merge_heaps(h1, h2)

print("Merged Heap:", merged_heap.heap)
