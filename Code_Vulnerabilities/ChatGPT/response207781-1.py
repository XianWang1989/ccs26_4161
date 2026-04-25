
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        # Compare nodes based solely on cost for heap sorting
        return self.cost < other.cost

# Perform an A* search to find the best path to the dirt
def aStar(self, current, end):
    openHeap = []  # All paths heap, lowest cost on top
    closedSet = set()  # Set of best paths (nodes)
    startNode = Node(None, current, self.manHatDist(current, end))
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curCost, curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)  # Use position to track closed nodes

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            # Calculate cost: g(n) + h(n)
            tile.cost = self.euclidDist(current, tile.pos) + self.manHatDist(tile.pos, end)
            tile.parent = curNode

            # Update logic: Check if node is already in heap
            if tile not in [h[1] for h in openHeap]:
                heapq.heappush(openHeap, (tile.cost, tile))

    return []

# Get the moves made to get to this endNode
def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves

# Example of calculating distances (assuming Manhattan distance is defined elsewhere)
def manHatDist(self, pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def euclidDist(self, pos1, pos2):
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5
