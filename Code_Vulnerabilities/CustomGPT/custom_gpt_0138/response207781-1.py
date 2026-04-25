
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        # Min-heap: prioritize by lowest cost
        return self.cost < other.cost

def aStar(self, current, end):
    openSet = set()
    openHeap = []
    closedSet = set()
    startNode = Node("", current, self.manHatDist(current, end))
    openSet.add(startNode)
    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile in closedSet:
                continue  # Skip already explored nodes

            tentative_cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

            if tile not in openSet or tentative_cost < tile.cost:
                tile.parent = curNode
                tile.cost = tentative_cost

                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, tile)

    return []

def getDirections(self, endNode):
    moves = []
    while endNode is not None:
        moves.append(endNode.value)
        endNode = endNode.parent
    moves.reverse()
    return moves

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))  # Set cost to zero, will be computed later
    return posMoves
