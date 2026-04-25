
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
    openHeap = []
    closedSet = {}
    start_node = Node(0, current, self.manHatDist(current, end))
    heapq.heappush(openHeap, start_node)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet[curNode.pos] = curNode.cost

        for tile in self.getAdjacentNodes(curNode.pos):
            new_cost = self.manHatDist(tile.pos, end) + curNode.cost

            if tile.pos in closedSet and new_cost >= closedSet[tile.pos]:
                continue

            tile.parent = curNode
            tile.cost = new_cost

            # Only add to the heap if not already present or found a cheaper cost
            heapq.heappush(openHeap, tile)

    return []

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
    return posMoves
