
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
    openHeap = []  # Priority queue for nodes to explore
    closedSet = set()  # Explored nodes
    startNode = Node('', current, self.manHatDist(current, end))

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
            tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

            # Only update if the tile is not already in the heap
            if (tile.cost, tile) not in openHeap:
                heapq.heappush(openHeap, (tile.cost, tile))

    return []

# The method to get directions remains the same
def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode and tmpNode.parent:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves
