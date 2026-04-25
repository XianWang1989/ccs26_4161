
class MaxHeap:
    def __init__(self, elements=None):
        self.heap = elements if elements else []
        self.build_max_heap()

    def build_max_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
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

def merge_heaps(h1, h2):
    return MaxHeap(h1.heap + h2.heap)

# Example usage
h1 = MaxHeap([10, 7, 9])
h2 = MaxHeap([8, 6, 5])

merged_heap = merge_heaps(h1, h2)
print(merged_heap.heap)  # Output: max heap structure
