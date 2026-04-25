
class MaxHeap:
    def __init__(self, elements):
        self.heap = self.build_max_heap(elements)

    def build_max_heap(self, elements):
        n = len(elements)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(elements, n, i)
        return elements

    def max_heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.max_heapify(arr, n, largest)

    def merge(self, h2):
        combined = self.heap + h2.heap
        return MaxHeap(combined)

h1 = MaxHeap([20, 15, 30])
h2 = MaxHeap([25, 10, 5])
merged_heap = h1.merge(h2)
print("Merged Heap:", merged_heap.heap)
