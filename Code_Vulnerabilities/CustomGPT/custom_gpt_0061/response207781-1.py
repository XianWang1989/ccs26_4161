
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Correctly implement less than

# A* search algorithm
def aStar(self, current, end):
    openSet = {}  # Dictionary for faster lookups
    openHeap = []  # Priority queue
    closedSet = set()  # Set for visited nodes

    startNode = Node(0, current, self.manHatDist(current, end))
    openSet[current] = startNode
    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            # Calculate new cost
            new_cost = self.manHatDist(tile.pos, end) + curNode.cost + 1  # Assumed that moving to adjacent tile has a cost of 1

            if tile.pos not in openSet or new_cost < openSet[tile.pos].cost:
                tile.cost = new_cost
                tile.parent = curNode

                if tile.pos not in openSet:
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, tile)

    return []

# Get directions from endNode to start
def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves

# Get adjacent nodes
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))  # cost is set to 0 here, will be adjusted later
    return posMoves
