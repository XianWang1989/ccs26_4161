
import heapq

# Replace the openHeap to be a priority queue directly:
openHeap = []
heapq.heappush(openHeap, (curNode.cost, curNode))
