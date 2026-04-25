
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

# Perform an A* search to find the best path
def aStar(self, current, end):
    openSet = {}  # Dictionary for explorable nodes
    openHeap = []  # All paths heap, lowest cost on top
    closedSet = set()  # Best path so far

    initial_cost = self.manHatDist(current, end)
    startNode = Node(0, current, initial_cost)
    openSet[current] = startNode
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]
        if curNode.pos == end:
            return self.getDirections(curNode)

        del openSet[curNode.pos]
        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            tile.parent = curNode
            tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

            if tile.pos not in openSet:
                openSet[tile.pos] = tile
                heapq.heappush(openHeap, (tile.cost, tile))
            elif tile.cost < openSet[tile.pos].cost:
                openSet[tile.pos] = tile
                heapq.heappush(openHeap, (tile.cost, tile))

    return []

# Get the moves made to get to this endNode
def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode and tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves

# Return all possible moves from given tile as Node objects
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            if newPos not in posMoves:  # Avoid duplicates
                posMoves.append(Node(direction, newPos, 0))
    return posMoves
