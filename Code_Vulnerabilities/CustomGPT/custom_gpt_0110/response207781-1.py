
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Direct cost comparison

def aStar(self, current, end):
    openSet = set()   # Set of explorable nodes
    openHeap = []     # All paths heap, lowest cost on top
    startNode = Node(None, current, 0)
    openSet.add(startNode)
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]
        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in openSet:
                tile.parent = curNode
                tile.cost = curNode.cost + self.manHatDist(tile.pos, end)
                if tile not in openSet:  # Avoid duplicates in openSet
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))
    return []

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            if newPos:  # Ensure new position is valid
                posMoves.append(Node(direction, newPos, 0))  # Cost is calculated later
    return posMoves

def getDirections(self, endNode):
    moves = []
    while endNode.parent is not None:
        moves.append(endNode.value)
        endNode = endNode.parent
    moves.reverse()
    return moves
