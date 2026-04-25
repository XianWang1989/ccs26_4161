
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
    openSet = {}  # Dictionary to store the node and its cost
    openHeap = []  # Min-heap for efficient retrieval
    closedSet = set()  # Set of best nodes
    start_cost = 0
    start_node = Node(None, current, start_cost + self.manHatDist(current, end))

    openSet[start_node.pos] = start_node.cost
    heapq.heappush(openHeap, start_node)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            # Calculate costs
            tentative_cost = curNode.cost + self.manHatDist(curNode.pos, tile.pos)

            if tile.pos not in openSet or tentative_cost < openSet[tile.pos]:
                tile.parent = curNode
                tile.cost = tentative_cost + self.manHatDist(tile.pos, end)
                openSet[tile.pos] = tentative_cost
                heapq.heappush(openHeap, tile)

    return []
