
class MaxHeap:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def insert(heap, value):
    # Add value to heap and maintain the max heap property
    # This will involve traversing the tree and placing the value appropriately
    pass  # Implementation of insertion here

def merge(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    if h1.value > h2.value:
        h1.right_child = merge(h1.right_child, h2)
        return h1
    else:
        h2.right_child = merge(h1, h2.right_child)
        return h2

# Usage
h1 = MaxHeap(10)
h2 = MaxHeap(20)
merged_heap = merge(h1, h2)
