
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
    openSet = {}  # Dictionary for tracking node costs
    openHeap = [] # Priority queue (min-heap)
    closedSet = set()

    startNode = Node(None, current, self.manHatDist(current, end))
    openSet[current] = startNode
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            tile.parent = curNode
            tentative_cost = curNode.cost + 1  # Assuming uniform cost for each move
            heuristic_cost = self.manHatDist(tile.pos, end)
            total_cost = tentative_cost + heuristic_cost

            if tile.pos not in openSet or tentative_cost < openSet[tile.pos].cost:
                tile.cost = total_cost
                openSet[tile.pos] = tile
                heapq.heappush(openHeap, (tile.cost, tile))

    return []
