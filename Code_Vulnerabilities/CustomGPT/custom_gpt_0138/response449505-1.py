
class MaxHeap:
    def __init__(self, elements=None):
        self.elements = elements or []

    def insert(self, value):
        self.elements.append(value)
        self._heapify_up(len(self.elements) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.elements[index] > self.elements[parent]:
                self.elements[index], self.elements[parent] = self.elements[parent], self.elements[index]
                index = parent
            else:
                break

def merge(h1, h2):
    # Create a new MaxHeap
    merged_heap = MaxHeap()

    # Insert all elements from h1 and h2 into the new heap
    for value in h1.elements:
        merged_heap.insert(value)
    for value in h2.elements:
        merged_heap.insert(value)

    return merged_heap
