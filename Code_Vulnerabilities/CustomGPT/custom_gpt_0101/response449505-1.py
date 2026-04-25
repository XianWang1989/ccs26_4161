
class MaxHeapNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def insert(heap, node):
    # Simple insert function to maintain max heap property.
    if heap is None:
        return node
    if node.value > heap.value:
        node.left_child = heap.left_child
        node.right_child = heap.right_child
        return node
    else:
        if heap.left_child is None:
            heap.left_child = node
        elif heap.right_child is None:
            heap.right_child = node
        else:
            if heap.left_child and (heap.right_child is None or heap.left_child.value > heap.right_child.value):
                insert(heap.left_child, node)
            else:
                insert(heap.right_child, node)
    return heap

def merge(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    if h1.value > h2.value:
        h1.left_child = merge(h1.left_child, h2)
        return h1
    else:
        h2.left_child = merge(h1, h2.left_child)
        return h2

# Example usage
h1 = MaxHeapNode(10)
h1.left_child = MaxHeapNode(5)
h1.right_child = MaxHeapNode(3)

h2 = MaxHeapNode(15)
h2.left_child = MaxHeapNode(8)
h2.right_child = MaxHeapNode(2)

merged_heap = merge(h1, h2)
