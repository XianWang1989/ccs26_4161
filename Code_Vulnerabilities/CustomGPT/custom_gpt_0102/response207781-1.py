
import heapq

# Perform an A* search to find the best path to the dirt
def aStar(self, current, end):
    openHeap = []  # Priority queue for the nodes to explore
    openSet = {}   # Dictionary to track nodes in openHeap
    closedSet = set()  # Set of evaluated nodes

    # Initialize the starting node
    startNode = Node(0, current, self.manHatDist(current, end))
    heapq.heappush(openHeap, (startNode.cost, startNode))
    openSet[startNode.pos] = startNode

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)
        del openSet[curNode.pos]

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            # Calculate the cost
            new_cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current) + curNode.cost

            if tile.pos not in openSet or new_cost < tile.cost:
                tile.cost = new_cost
                tile.parent = curNode

                if tile.pos not in openSet:
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []

# Node class for A* search - unchanged
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost
