
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
    openSet = set()
    openHeap = []
    closedSet = {}

    startNode = Node(0, current, self.manHatDist(current, end))
    openSet.add(startNode)
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        _, curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet[curNode.pos] = curNode.cost

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet and closedSet[tile.pos] <= tile.cost:
                continue

            tile.parent = curNode
            tile.cost = self.manHatDist(tile.pos, end) + curNode.cost

            if tile not in openSet:
                openSet.add(tile)
                heapq.heappush(openHeap, (tile.cost, tile))

    return []

def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves
