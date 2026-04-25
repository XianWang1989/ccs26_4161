
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Corrected the comparison logic

def aStar(self, current, end):
    openSet = {}  # Dictionary to track nodes in the open set
    openHeap = []  # List to behave as a min-heap
    closedSet = set()

    startNode = Node(None, current, 0)
    startNode.cost = self.manHatDist(current, end)
    heapq.heappush(openHeap, (startNode.cost, startNode))
    openSet[current] = startNode

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.pop(curNode.pos)
        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            # Cost calculation (only once)
            tile.parent = curNode
            tile.cost = self.manHatDist(tile.pos, end) + \
                        self.euclidDist(current, curNode.pos) + \
                        (curNode.cost - self.manHatDist(curNode.pos, end))

            if tile.pos not in openSet or tile.cost < openSet[tile.pos].cost:
                openSet[tile.pos] = tile
                heapq.heappush(openHeap, (tile.cost, tile))

    return []

def getDirections(self, endNode):
    moves = []
    while endNode.parent is not None:
        moves.append(endNode.value)
        endNode = endNode.parent
    moves.reverse()
    return moves

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            nextPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, nextPos, 0))
    return posMoves
