
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.value = value
        self.pos = pos
        self.cost = cost
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

def aStar(self, current, end):
    openSet = set()   # Set of explorable nodes
    openHeap = []     # All paths heap, lowest cost on top
    startNode = Node(None, current, self.manHatDist(current, end))
    openSet.add(startNode)
    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in openSet:
                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + curNode.cost

                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, tile)

    return []

def getDirections(self, endNode):
    moves = []
    while endNode.parent is not None:
        moves.append(endNode.value)
        endNode = endNode.parent
    moves.reverse()
    return moves

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))  # Cost is initialized to 0; it will be calculated later
    return posMoves
