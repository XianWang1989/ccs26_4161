
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

def aStar(self, current, end):
    openHeap = []        # Priority queue for exploring nodes (min-heap)
    closedSet = set()    # Set of already explored nodes
    startNode = Node(0, current, self.manHatDist(current, end))
    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)   # Add current node position to closed set

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            tile.parent = curNode
            tile.cost = curNode.cost + self.manHatDist(tile.pos, end)

            # Avoid adding nodes to openHeap if they have a higher cost already in the heap
            if tile not in openHeap:
                heapq.heappush(openHeap, tile)

    return []
