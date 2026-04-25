
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
    openSet = {}
    openHeap = []
    closedSet = set()
    startNode = Node('', current, self.manHatDist(current, end))

    openSet[current] = startNode
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]
        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.pop(curNode.pos)
        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue
            tile.parent = curNode
            tile.cost = self.manHatDist(tile.pos, end)

            if tile.pos not in openSet or tile.cost < openSet[tile.pos].cost:
                openSet[tile.pos] = tile
                heapq.heappush(openHeap, (tile.cost, tile))

    return []
