
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
    openHeap = []  # Priority queue for nodes to explore
    closedSet = set()  # Explored nodes

    startNode = Node("", current, self.manHatDist(current, end))
    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            tile.parent = curNode
            newCost = curNode.cost + 1  # Assuming uniform cost for adjacent moves
            if not any(openNode.pos == tile.pos and openNode.cost <= newCost for openNode in openHeap):
                tile.cost = newCost + self.manHatDist(tile.pos, end)
                heapq.heappush(openHeap, tile)

    return []

def getAdjacentNodes(self, curPos):
    directions = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in directions:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))
    return posMoves
