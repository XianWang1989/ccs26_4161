
class MaxHeap:
    def __init__(self):
        self.elements = []

    def insert(self, key):
        self.elements.append(key)
        self._heapify_up(len(self.elements) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.elements[index] > self.elements[parent_index]:
            self.elements[index], self.elements[parent_index] = self.elements[parent_index], self.elements[index]
            self._heapify_up(parent_index)

    def merge(self, other):
        for element in other.elements:
            self.insert(element)

# Example usage
h1 = MaxHeap()
h1.insert(10)
h1.insert(5)
h1.insert(3)

h2 = MaxHeap()
h2.insert(8)
h2.insert(6)

# Merging
h1.merge(h2)

print(h1.elements)  # This should print a valid max heap
