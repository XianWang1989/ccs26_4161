
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def build_max_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

def merge_heaps(h1, h2):
    new_heap = MaxHeap()
    new_heap.build_max_heap(h1.heap + h2.heap)
    return new_heap

# Example usage:
heap1 = MaxHeap()
heap1.insert(10)
heap1.insert(5)
heap1.insert(30)

heap2 = MaxHeap()
heap2.insert(20)
heap2.insert(3)
heap2.insert(25)

merged_heap = merge_heaps(heap1, heap2)
print("Merged Heap:", merged_heap.heap)  # Should maintain max heap properties.
