
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

# Perform an A* search to find the best path to the goal
def aStar(self, current, end):
    openSet = set()  # Set of explorable nodes
    openHeap = []    # All paths heap, lowest cost on top
    startNode = Node('', current, 0)
    openSet.add(startNode)
    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile in openSet:  # Skip if already in openSet
                continue

            tile.parent = curNode
            tile.cost = self.calculateCost(tile, end, current)
            if tile not in openSet:
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

# Calculate the cost of a node
def calculateCost(self, tile, end, current):
    return self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

# Return all possible moves from given tile as Node objects
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            nextPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, nextPos, 0))
    return posMoves
