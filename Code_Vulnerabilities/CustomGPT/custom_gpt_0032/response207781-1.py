
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
    openSet = {}  # Use a dictionary to track nodes in the open set
    openHeap = []  # Priority queue for processing nodes
    closedSet = set()  # Set of nodes already evaluated

    startNode = Node('', current, self.manHatDist(current, end))
    openSet[current] = startNode
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        closedSet.add(curNode.pos)
        del openSet[curNode.pos]

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            newCost = curNode.cost + self.manHatDist(curNode.pos, tile.pos)

            if tile.pos not in openSet or newCost < openSet[tile.pos].cost:
                tile.parent = curNode
                tile.cost = newCost
                openSet[tile.pos] = tile

                if tile not in [h[1] for h in openHeap]:  # Only add if not in the heap
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []

def getDirections(self, endNode):
    moves = []
    while endNode is not None:
        moves.append(endNode.value)
        endNode = endNode.parent
    return moves[::-1]  # Reverse to get the correct order

def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            newPos = self.getLocIfMove(curPos, direction)
            posMoves.append(Node(direction, newPos, 0))
    return posMoves
