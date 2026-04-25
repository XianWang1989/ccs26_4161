
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

# Perform an A* search to find the best path
def aStar(self, current, end):
    openSet = {}  # Dictionary for explorable nodes
    openHeap = []  # Min-heap for node costs
    closedSet = set()  # Set of already explored nodes

    start_node = Node(None, current, self.manHatDist(current, end))
    openSet[current] = start_node
    heapq.heappush(openHeap, (start_node.cost, start_node))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)
        del openSet[curNode.pos]

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue  # Skip if already explored

            tile_cost = self.manHatDist(tile.pos, end) + self.euclidDist(curNode.pos, current) + curNode.cost

            if tile.pos not in openSet or tile_cost < openSet[tile.pos].cost:
                tile.parent = curNode
                tile.cost = tile_cost
                openSet[tile.pos] = tile
                heapq.heappush(openHeap, (tile.cost, tile))

    return []

# Get the moves made to get to this endNode
def getDirections(self, endNode):
    moves = []
    while endNode.parent is not None:
        moves.append(endNode.value)
        endNode = endNode.parent
    moves.reverse()
    return moves

# Get all possible moves from given tile as Node objects
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            next_pos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, next_pos, 0))
    return posMoves
