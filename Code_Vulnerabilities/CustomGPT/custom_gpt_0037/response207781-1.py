
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

# A* search algorithm
def aStar(self, current, end):
    openHeap = []
    closedSet = set()

    startNode = Node(None, current, self.manHatDist(current, end))
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            tile.parent = curNode
            tile.cost = self.manHatDist(tile.pos, end) + curNode.cost  # Simplified cost calculation

            if tile not in [n[1] for n in openHeap]:  # Check if not already in openHeap
                heapq.heappush(openHeap, (tile.cost, tile))

    return []

# Directions retrieval
def getDirections(self, endNode):
    moves = []
    while endNode.parent is not None:
        moves.append(endNode.value)
        endNode = endNode.parent
    return moves[::-1]
