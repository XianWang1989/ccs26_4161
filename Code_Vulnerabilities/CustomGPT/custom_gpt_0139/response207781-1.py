
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
    openSet = set()   # Set of explorable nodes
    openHeap = []     # All paths heap, lowest cost on top
    startNode = Node("", current, 0)
    heapq.heappush(openHeap, (0, startNode)) # Start with initial node

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        if curNode.pos in openSet:
            continue  # Skip if already processed
        openSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos not in openSet:
                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current) + curNode.cost
                # Check if tile is already in openHeap, and update if needed
                for _, node in openHeap:
                    if node.pos == tile.pos and node.cost <= tile.cost:
                        break
                else:
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []
