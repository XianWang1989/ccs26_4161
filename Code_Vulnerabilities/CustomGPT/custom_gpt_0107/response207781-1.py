
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Correct comparison for priority queue

def aStar(self, current, end):
    openSet = set()
    openHeap = []
    closedSet = set()

    startNode = Node(0, current, self.manHatDist(current, end))
    openSet.add(startNode)
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:  # Use openHeap for faster extraction
        curNode = heapq.heappop(openHeap)[1]
        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile in closedSet:
                continue

            new_cost = self.euclidDist(current, tile.pos) + self.manHatDist(tile.pos, end)

            if tile not in openSet or new_cost < tile.cost:
                tile.cost = new_cost
                tile.parent = curNode

                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []
