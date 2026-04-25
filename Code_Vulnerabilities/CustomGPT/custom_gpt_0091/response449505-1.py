
class MaxHeap:
    def __init__(self, values=[]):
        self.heap = values
        self.build_max_heap()

    def build_max_heap(self):
        n = len(self.heap)
        for i in range(n // 2, -1, -1):
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

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

def merge_heaps(h1, h2):
    merged_heap = MaxHeap()
    for value in h1.heap:
        merged_heap.insert(value)
    for value in h2.heap:
        merged_heap.insert(value)
    return merged_heap

# Example usage:
h1 = MaxHeap([10, 7, 5])
h2 = MaxHeap([8, 6, 4])
merged = merge_heaps(h1, h2)
print(merged.heap)  # Output the merged heap
