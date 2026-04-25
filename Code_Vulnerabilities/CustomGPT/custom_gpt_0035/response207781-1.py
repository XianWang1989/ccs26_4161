
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Changed to use a standard comparison

def aStar(self, current, end):
    openHeap = []  # Priority queue for the nodes to explore
    openSet = {}   # Dictionary to track nodes in the open set
    closedSet = set()  # Set for explored nodes

    startNode = Node(0, current, self.manHatDist(current, end))
    heapq.heappush(openHeap, startNode)
    openSet[current] = startNode  # Store nodes by their position

    while openHeap:
        curNode = heapq.heappop(openHeap)
        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)
        del openSet[curNode.pos]

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue  # Skip if already evaluated

            tile_cost = self.manHatDist(tile.pos, end) + curNode.cost + 1  # Assuming uniform cost of 1 for movement

            if tile.pos not in openSet or tile_cost < openSet[tile.pos].cost:
                tile.cost = tile_cost
                tile.parent = curNode

                if tile.pos not in openSet:
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, tile)

    return []

# Ensure getDirections remains unchanged
