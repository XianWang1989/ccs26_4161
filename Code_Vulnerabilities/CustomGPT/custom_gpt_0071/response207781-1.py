
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

def aStar(self, current, end):
    openSet = {}  # Dictionary to store nodes and their costs
    openHeap = []  # Priority queue for nodes

    startNode = Node(0, current, self.manHatDist(current, end))
    openSet[startNode.pos] = startNode
    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        del openSet[curNode.pos]

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in openSet:
                continue

            tile.parent = curNode
            tile.cost = self.manHatDist(tile.pos, end) + (curNode.cost - self.manHatDist(curNode.pos, end)) + 1

            if tile.pos not in openSet:
                openSet[tile.pos] = tile
                heapq.heappush(openHeap, tile)

    return []

def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves

# Get adjacent nodes method remains unchanged
