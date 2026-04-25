
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def merge(self, h2):
        for value in h2.heap:
            self.insert(value)

# Example usage
h1 = MaxHeap()
h1.insert(10)
h1.insert(20)

h2 = MaxHeap()
h2.insert(5)
h2.insert(15)

h1.merge(h2)

print(h1.heap)  # Output should be a valid max heap
