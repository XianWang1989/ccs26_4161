
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

def merge_heaps(h1, h2):
    merged_heap = MaxHeap()

    for value in h1.heap:
        merged_heap.insert(value)
    for value in h2.heap:
        merged_heap.insert(value)

    return merged_heap.heap

# Example usage
h1 = MaxHeap()
h2 = MaxHeap()
h1.insert(10)
h1.insert(20)
h1.insert(30)

h2.insert(5)
h2.insert(15)

merged = merge_heaps(h1, h2)
print("Merged Heap:", merged)
