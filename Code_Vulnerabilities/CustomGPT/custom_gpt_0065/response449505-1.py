
class MaxHeap:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self._heapify_up(len(self.data) - 1)

    def _heapify_up(self, index):
        # Implementation of heapify up
        pass

def merge(h1, h2):
    if len(h1.data) == 0:
        return h2
    if len(h2.data) == 0:
        return h1

    combined_data = h1.data + h2.data
    merged_heap = MaxHeap()

    for value in combined_data:
        merged_heap.insert(value)

    return merged_heap
