
class MaxHeap:
    def __init__(self, elements):
        self.heap = elements
        self.build_max_heap()

    def build_max_heap(self):
        for i in range(len(self.heap) // 2, -1, -1):
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
    new_heap = h1 + h2  # Concatenate both heaps
    return MaxHeap(new_heap).heap  # Build max heap

# Example usage:
h1 = [10, 7, 3]
h2 = [15, 14, 8]
merged_heap = merge_heaps(h1, h2)
print("Merged Max Heap:", merged_heap)
