
class MaxHeapNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def insert(heap, node):
    # Logic to insert node into the heap
    # This function will maintain heap properties
    pass

def merge(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    if h1.value > h2.value:
        h1, h2 = h2, h1  # Ensure h1 is the bigger one

    # Merge two nodes
    if h1.left_child is None:
        h1.left_child = h2
    elif h1.right_child is None:
        h1.right_child = h2
    else:
        # Recursively merge one of the children
        orphan = merge(h1.left_child, h2)
        if h1.left_child.value >= h1.right_child.value:
            h1.right_child = orphan
        else:
            h1.left_child = orphan

    return h1

# Example Usage
root1 = MaxHeapNode(10)
root1.left_child = MaxHeapNode(5)
root1.right_child = MaxHeapNode(6)

root2 = MaxHeapNode(12)
root2.left_child = MaxHeapNode(8)

merged_heap = merge(root1, root2)
