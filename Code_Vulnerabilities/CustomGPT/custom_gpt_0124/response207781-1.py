
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
    openHeap = []      # Priority queue for unexplored nodes
    closedSet = set()  # Set of nodes already evaluated
    startNode = Node('', current, 0 + self.manHatDist(current, end))

    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos not in closedSet:
                tile.parent = curNode
                tile.cost = curNode.cost + 1 + self.manHatDist(tile.pos, end)  # Update cost

                if not any(t.pos == tile.pos and t.cost <= tile.cost for t in openHeap):
                    heapq.heappush(openHeap, tile)

    return []

def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
    return posMoves
