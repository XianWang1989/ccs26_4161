
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Reverse logic for min-heap

def aStar(self, current, end):
    openSet = set()  # Set of explorable nodes
    openHeap = []    # All paths heap, lowest cost on top
    closedSet = set()  # Best path so far
    curNode = Node(0, current, self.manHatDist(current, end))
    openSet.add(curNode)
    heapq.heappush(openHeap, curNode)  # Directly push the node

    while openHeap:
        curNode = heapq.heappop(openHeap)
        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in closedSet:
                tentative_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos)
                if tile not in openSet or tentative_cost < tile.cost:  
                    tile.cost = tentative_cost + self.manHatDist(tile.pos, end)
                    tile.parent = curNode
                    if tile not in openSet:
                        openSet.add(tile)
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

# Return all possible moves from given tile as Node objects
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
    return posMoves
