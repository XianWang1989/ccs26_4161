
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)

    def bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] < self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def merge(self, other):
        for value in other.heap:
            self.insert(value)

def merge_heaps(h1, h2):
    new_heap = MaxHeap()
    new_heap.heap = h1.heap[:]  # Copy the heap
    new_heap.merge(h2)  # Merge the second heap
    return new_heap

# Example usage
h1 = MaxHeap()
h1.insert(10)
h1.insert(5)
h1.insert(30)

h2 = MaxHeap()
h2.insert(20)
h2.insert(25)

# Merging heaps h1 and h2
merged_heap = merge_heaps(h1, h2)
print(merged_heap.heap)  # Output will represent the merged heap
