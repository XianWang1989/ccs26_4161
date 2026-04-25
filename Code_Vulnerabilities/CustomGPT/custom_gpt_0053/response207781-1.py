
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost  # g + h
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

def aStar(self, current, end):
    openSet = {}  # Dict for the node with position as keys
    openHeap = []  # Priority queue
    closedSet = set()  # Set to track visited nodes

    # Initial node
    startNode = Node(0, current, self.manHatDist(current, end))
    openSet[current] = startNode
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        # Move node from open to closed
        openSet.pop(curNode.pos)
        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            # Calculate costs
            tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current) + curNode.cost

            if tile.pos not in openSet or tile.cost < openSet[tile.pos].cost:
                tile.parent = curNode
                openSet[tile.pos] = tile
                heapq.heappush(openHeap, (tile.cost, tile))

    return []

def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            next_pos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, next_pos, 0))
    return posMoves
