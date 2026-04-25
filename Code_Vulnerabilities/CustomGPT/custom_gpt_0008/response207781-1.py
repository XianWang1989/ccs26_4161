
import heapq

# Updated Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Compare based on cost

    def __eq__(self, other):
        return self.pos == other.pos  # Ensure uniqueness by position


# Perform an A* search to find the best path
def aStar(self, current, end):
    openHeap = []     # Min-heap for exploring nodes
    closedSet = set() # Set of explored nodes
    curNode = Node("", current, self.manHatDist(current, end))
    heapq.heappush(openHeap, (curNode.cost, curNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile in closedSet:
                continue

            g_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos)
            tile_cost = g_cost + self.manHatDist(tile.pos, end)

            if not any(openNode.pos == tile.pos and openNode.cost <= tile_cost for openNode in openHeap):
                tile.parent = curNode
                tile.cost = tile_cost
                heapq.heappush(openHeap, (tile.cost, tile))

    return []

# Get the moves made to reach this endNode
def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves

# Get all possible moves from given tile as Node objects
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))
    return posMoves
