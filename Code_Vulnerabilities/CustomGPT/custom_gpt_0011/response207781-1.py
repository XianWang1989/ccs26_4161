
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
    openSet = {}  # Dictionary for open set
    openHeap = []  # Priority queue for nodes
    closedSet = set()  # Set of best path nodes

    startNode = Node(0, current, self.manHatDist(current, end))
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

            # Calculate tentative cost
            tentative_g_score = curNode.cost + self.euclidDist(curNode.pos, tile.pos)
            if tile.pos not in openSet or tentative_g_score < tile.cost:
                tile.parent = curNode
                tile.cost = tentative_g_score + self.manHatDist(tile.pos, end)

                if tile.pos not in openSet:
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []

# The method getDirections remains unchanged.
