
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Correct comparison for heap operations

# A* algorithm implementation
def aStar(self, current, end):
    openSet = set()   # Set of explorable nodes
    openHeap = []     # All paths heap, lowest cost on top
    curNode = Node(0, current, self.manHatDist(current, end))

    openSet.add(curNode)
    heapq.heappush(openHeap, curNode)  # Push node directly, no tuple needed

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in openSet:
                tile.parent = curNode
                tile.cost = self.euclidDist(tile.pos, current) + self.manHatDist(tile.pos, end)
                if tile not in openSet:  # Only add if not already explored
                    openSet.add(tile)
                    heapq.heappush(openHeap, tile)

    return []

# Get the moves made to get to this endNode
def getDirections(self, endNode):
    moves = []
    while endNode.parent is not None:
        moves.append(endNode.value)
        endNode = endNode.parent
    moves.reverse()
    return moves

# Return all possible moves from given tile as Node objects
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))  # Cost initialized to 0; calculated later
    return posMoves
