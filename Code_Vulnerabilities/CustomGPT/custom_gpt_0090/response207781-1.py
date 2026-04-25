
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

# A* algorithm implementation
def aStar(self, current, end):
    openSet = {}  # Dictionary to quickly check existence
    openHeap = []  # Min-heap for tracking lowest cost
    closedSet = set()  # Explored nodes

    startNode = Node(0, current, self.manHatDist(current, end))
    openSet[startNode.pos] = startNode
    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)
        del openSet[curNode.pos]

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current) + curNode.cost
            tile.parent = curNode

            if tile.pos not in openSet or tile.cost < openSet[tile.pos].cost:
                openSet[tile.pos] = tile
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

# Get adjacent nodes method
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
    return posMoves
