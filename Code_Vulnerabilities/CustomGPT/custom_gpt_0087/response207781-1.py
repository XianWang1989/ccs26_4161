
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
    openSet = []  # Priority queue for lowest cost next
    closedSet = set()  # Explored nodes
    startNode = Node("", current, 0 + self.manHatDist(current, end))
    heapq.heappush(openSet, startNode)

    while openSet:
        curNode = heapq.heappop(openSet)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            # Calculate costs only once
            tile.parent = curNode
            tile.cost = curNode.cost + 1 + self.manHatDist(tile.pos, end)

            if tile not in openSet:
                heapq.heappush(openSet, tile)

    return []

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))
    return posMoves

def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    return moves[::-1]  # Reverse the moves
