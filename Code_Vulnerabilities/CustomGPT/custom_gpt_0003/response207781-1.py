
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Proper comparison for heap

# Perform an A* search to find the best path to the end
def aStar(self, current, end):
    openSet = {}  # Use a dictionary for tracking explorable nodes
    openHeap = []  # For performance, use heapq as priority queue
    closedSet = set()  # Best path so far

    # Initialize the starting node with its cost
    start_node = Node(None, current, self.manHatDist(current, end))
    openSet[current] = start_node
    heapq.heappush(openHeap, (start_node.cost, start_node))

    while openHeap:
        # Get the node with the lowest cost
        curNode = heapq.heappop(openHeap)[1]

        # Check if we reached the end
        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)
        del openSet[curNode.pos]  # Remove node from open set

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            tile.cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos) + self.manHatDist(tile.pos, end)
            tile.parent = curNode

            if tile.pos not in openSet or tile.cost < openSet[tile.pos].cost:
                openSet[tile.pos] = tile
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

# Definition of getAdjacentNodes method unchanged
