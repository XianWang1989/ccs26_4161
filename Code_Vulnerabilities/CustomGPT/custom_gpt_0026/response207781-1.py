
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # For min-heap

# Perform an A* search to find the best path to the target
def aStar(self, current, end):
    openSet = {}   # Use a dictionary for open set
    openHeap = []  # Min-heap for node exploration
    closedSet = set()  # Explored nodes

    startNode = Node(0, current, self.manHatDist(current, end))
    openSet[current] = startNode
    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            new_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos)
            if tile.pos not in openSet or new_cost < openSet[tile.pos].cost:
                tile.parent = curNode
                tile.cost = new_cost + self.manHatDist(tile.pos, end)
                openSet[tile.pos] = tile  # Update open set
                heapq.heappush(openHeap, tile)

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
