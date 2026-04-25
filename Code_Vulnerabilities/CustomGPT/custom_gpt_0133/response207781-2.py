
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    # Use total_ordering for better comparability
    def __lt__(self, other):
        return self.cost < other.cost

def aStar(self, current, end):
    openSet = {}  # Using dictionary for efficient lookups
    openHeap = []  # Priority queue based on cost
    closedSet = set()  # Closed nodes
    curNode = Node(None, current, 0)
    openSet[curNode.pos] = curNode
    heapq.heappush(openHeap, (curNode.cost, curNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]
        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.pop(curNode.pos, None)  # Remove from openSet
        closedSet.add(curNode.pos)  # Add to closedSet

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            # Calculate the cost once
            tile.cost = curNode.cost + self.manHatDist(tile.pos, end)  # Only use heuristic cost here
            tile.parent = curNode

            if tile.pos not in openSet or tile.cost < openSet[tile.pos].cost:
                openSet[tile.pos] = tile  # Add or update tile
                heapq.heappush(openHeap, (tile.cost, tile))

    return []

def getDirections(self, endNode):
    moves = []
    while endNode.parent is not None:
        moves.append(endNode.value)
        endNode = endNode.parent
    moves.reverse()
    return moves

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            neighbor_pos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, neighbor_pos, 0))  # Limit cost at initialization
    return posMoves
