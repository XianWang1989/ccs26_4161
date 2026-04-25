
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

def aStar(self, current, end):
    openSet = {}  # Use a dictionary for fast look-up
    openHeap = []  # Min-heap for paths
    closedSet = set()  # Track explored nodes

    startNode = Node(None, current, 0)
    startNode.cost = self.manHatDist(current, end)
    openSet[current] = startNode
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.pop(curNode.pos)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            tentative_cost = curNode.cost + 1  # Assuming uniform cost for simplicity
            if tile.pos not in openSet or tentative_cost < tile.cost:
                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + tentative_cost

                if tile.pos not in openSet:
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []

def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode.parent:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves

def getAdjacentNodes(self, curPos):
    directions = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in directions:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))
    return posMoves
