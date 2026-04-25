
class MaxHeap:
    def __init__(self, data=None):
        self.data = data if data else []

    def insert(self, val):
        self.data.append(val)
        self._heapify_up(len(self.data) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[parent] < self.data[index]:
                self.data[parent], self.data[index] = self.data[index], self.data[parent]
                index = parent
            else:
                break

    def build_max_heap(self):
        # Build the max heap (not shown for brevity)
        pass

def merge(h1, h2):
    # Concatenate the arrays from both heaps
    new_heap_data = h1.data + h2.data
    new_heap = MaxHeap(new_heap_data)
    new_heap.build_max_heap()  # Ensure it satisfies max heap property
    return new_heap

# Example Usage
heap1 = MaxHeap([10, 5, 3])
heap2 = MaxHeap([8, 7, 6])
merged_heap = merge(heap1, heap2)

print(merged_heap.data)  # Output will be the merged max heap
