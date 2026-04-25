
class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def insert(heap, node):
    # Simplified insert function for a max heap
    if heap is None:
        return node
    if node.value > heap.value:
        node, heap = heap, node
    if heap.left_child is None:
        heap.left_child = insert(heap.left_child, node)
    elif heap.right_child is None:
        heap.right_child = insert(heap.right_child, node)
    else:
        if heap.left_child.value > heap.right_child.value:
            heap.right_child = insert(heap.right_child, node)
        else:
            heap.left_child = insert(heap.left_child, node)
    return heap

def merge(h1, h2):
    if h1 is None: return h2
    if h2 is None: return h1
    if h1.value > h2.value:
        h1, h2 = h2, h1

    h1.right_child = merge(h1.right_child, h2)
    return h1

# Example Usage
h1 = Node(10)
h1.left_child = Node(7)
h1.right_child = Node(9)

h2 = Node(15)
h2.left_child = Node(13)
h2.right_child = Node(12)

merged_heap = merge(h1, h2)
