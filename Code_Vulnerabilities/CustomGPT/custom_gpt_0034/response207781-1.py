
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

# Perform an A* search to find the best path to the dirt
def aStar(self, current, end):
    openSet = set()   # Set of explorable nodes
    openHeap = []     # All paths heap, lowest cost on top
    closedSet = set() # Best path so far

    startNode = Node('Start', current, self.manHatDist(current, end))
    openSet.add(current)
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode.pos)
        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos not in closedSet and tile.pos not in openSet:
                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + curNode.cost
                openSet.add(tile.pos)
                heapq.heappush(openHeap, (tile.cost, tile))
            elif tile.pos in openSet:
                if tile.cost < curNode.cost:  # Check if we found a better path
                    tile.parent = curNode
                    tile.cost = self.manHatDist(tile.pos, end) + curNode.cost
                    heapq.heappush(openHeap, (tile.cost, tile))
    return []

# Get the moves made to get to this endNode
def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves

# Return all possible moves from given tile as Node objects
def getAdjacentNodes(self, curPos):
    allMoves = ['North','South','East','West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))
    return posMoves
