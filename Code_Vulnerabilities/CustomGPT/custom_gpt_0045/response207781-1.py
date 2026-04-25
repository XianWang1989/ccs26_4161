
import heapq  # Ensure you have this import at the top of your code

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

# Perform an A* search to find the best path to the target
def aStar(self, current, end):
    openSet = set()   # Set of explorable nodes
    openHeap = []     # All paths heap, lowest cost on top
    closedSet = set() # Best path so far

    startNode = Node(0, current, self.manHatDist(current, end))
    openSet.add(startNode)
    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in closedSet:
                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(curNode.pos, current) + curNode.cost

                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, tile)

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
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []

    for direction in allMoves:
        newPos = self.getLocIfMove(curPos, direction)  # Position after the move
        if newPos and self.canMove(direction, curPos):  # Check if the move is valid
            posMoves.append(Node(direction, newPos, 0))  # Only need to use the position
    return posMoves
