
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Comparison for priority queue

# Perform an A* search to find the best path to the dirt
def aStar(self, current, end):
    openSet = dict()   # Change set to dictionary for O(1) lookups
    openHeap = []      # All paths heap, lowest cost on top
    closedSet = set()  # Best path so far

    startNode = Node("", current, 0)
    openSet[current] = startNode
    heapq.heappush(openHeap, (0, startNode))  # Push initial node with cost 0

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)
        del openSet[curNode.pos]

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            g_cost = curNode.cost + 1  # Assuming uniform cost
            h_cost = self.manHatDist(tile.pos, end)  # Use only heuristic for cost prediction
            tile.cost = g_cost + h_cost
            tile.parent = curNode

            if tile.pos not in openSet:  # Not yet in open set
                openSet[tile.pos] = tile
                heapq.heappush(openHeap, (tile.cost, tile))
            else:  # In open set, check if we found a better path
                if g_cost < openSet[tile.pos].cost:
                    openSet[tile.pos].cost = tile.cost
                    openSet[tile.pos].parent = curNode

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
