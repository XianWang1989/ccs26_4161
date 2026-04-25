
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.value = value
        self.pos = pos
        self.cost = cost
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Correct comparison for priority queue

def aStar(self, current, end):
    openSet = []
    closedSet = set()
    startNode = Node(None, current, self.manHatDist(current, end))
    heapq.heappush(openSet, startNode)

    while openSet:
        curNode = heapq.heappop(openSet)
        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            tile.parent = curNode
            tile.cost = self.manHatDist(tile.pos, end) + curNode.cost

            # Check if tile is in openSet already
            if tile not in openSet:
                heapq.heappush(openSet, tile)

    return []

def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))  # Cost is handled in aStar
    return posMoves
