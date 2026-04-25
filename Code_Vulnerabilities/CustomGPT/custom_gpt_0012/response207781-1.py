
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

def aStar(self, current, end):
    openSet = set()   # Set of explorable nodes
    openHeap = []     # All paths heap, lowest cost on top
    curNode = Node(0, current, self.manHatDist(current, end))
    openSet.add(curNode)
    heapq.heappush(openHeap, curNode)

    while openHeap:  # Check the heap, not openSet directly
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in openSet:  # Check if already in the open set
                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current) + curNode.cost
                openSet.add(tile)
                heapq.heappush(openHeap, tile)
            else:
                # If it's already in the open set, check if we found a better path
                if tile.cost < curNode.cost:
                    tile.parent = curNode
                    heapq.heapify(openHeap)  # Re-heapify to maintain correct order

    return []

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
    return posMoves

def getDirections(self, endNode):
    moves = []
    tmpNode = endNode
    while tmpNode.parent is not None:
        moves.append(tmpNode.value)
        tmpNode = tmpNode.parent
    moves.reverse()
    return moves
