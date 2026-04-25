
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

    def __eq__(self, other):
        return self.pos == other.pos  # Nodes are equal based on position

# Perform an A* search to find the best path to the dirt
def aStar(self, current, end):
    openSet = set()
    openHeap = []
    closedSet = set()

    startNode = Node('Start', current, self.manHatDist(current, end))
    openSet.add(startNode)
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        _, curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)  # Remove from open set
        closedSet.add(curNode.pos)  # Add position to closed set

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos not in closedSet:
                tentative_cost = curNode.cost + 1  # Account for movement cost
                if tile not in openSet or tentative_cost < tile.cost:
                    tile.parent = curNode
                    tile.cost = tentative_cost + self.manHatDist(tile.pos, end)  # g + h
                    if tile not in openSet:
                        openSet.add(tile)
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

# Return all possible moves from given tile as Node objects
def getAdjacentNodes(self, curPos):
    allMoves = {'North': (0, 1), 'South': (0, -1), 'East': (1, 0), 'West': (-1, 0)}
    posMoves = []
    for direction, (dx, dy) in allMoves.items():
        newPos = (curPos[0] + dx, curPos[1] + dy)
        if self.canMove(direction, curPos):
            posMoves.append(Node(direction, newPos, 0))  # cost is set elsewhere
    return posMoves
