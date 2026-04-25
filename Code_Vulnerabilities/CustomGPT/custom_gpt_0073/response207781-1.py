
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
    openSet = []
    closedSet = set()

    startNode = Node(0, current, self.manHatDist(current, end))
    heapq.heappush(openSet, startNode)

    while openSet:
        curNode = heapq.heappop(openSet)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            tentative_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos) + self.manHatDist(tile.pos, end)

            if not any(node.pos == tile.pos and node.cost <= tentative_cost for node in openSet):
                tile.cost = tentative_cost
                tile.parent = curNode
                heapq.heappush(openSet, tile)

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
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))  # Cost will be set in A* directly
    return posMoves
