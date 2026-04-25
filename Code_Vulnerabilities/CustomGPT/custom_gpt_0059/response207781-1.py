
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

# A* algorithm
def aStar(self, current, end):
    openSet = {}  # Dictionary to track open set for O(1) lookups
    openHeap = []  # Priority queue for nodes to explore
    closedSet = set()  # Set for visited nodes
    startNode = Node("", current, self.manHatDist(current, end))

    openSet[current] = startNode
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        _, curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)
        del openSet[curNode.pos]

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            newCost = curNode.cost + self.manHatDist(tile.pos, end)
            if tile.pos not in openSet or newCost < openSet[tile.pos].cost:
                tile.parent = curNode
                tile.cost = newCost

                if tile.pos not in openSet:
                    openSet[tile.pos] = tile
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

# Get adjacent nodes
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))
    return posMoves
