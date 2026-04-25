
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    # Single comparison method based on cost
    def __lt__(self, other):
        return self.cost < other.cost

# A* search implementation
def aStar(self, current, end):
    openSet = set()  # Set of explorable nodes
    openHeap = []    # Priority queue for lowest cost
    closedSet = set()  # Explored nodes
    curNode = Node(0, current, self.manHatDist(current, end))
    openSet.add(curNode)
    heapq.heappush(openHeap, curNode)  # Use only Node

    while openHeap:
        curNode = heapq.heappop(openHeap)
        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in closedSet:
                tile.parent = curNode
                # Calculate costs only once per Node
                tile_cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

                if tile not in openSet or tile.cost > tile_cost:
                    tile.cost = tile_cost
                    if tile not in openSet:
                        openSet.add(tile)
                        heapq.heappush(openHeap, tile)  # Push Node directly

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

# Get adjacent nodes, minimizing Node creation
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))  # Cost will be set later
    return posMoves
