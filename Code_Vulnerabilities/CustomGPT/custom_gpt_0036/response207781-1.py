
import heapq

# Node class for A* search
class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __hash__(self):
        return hash(self.pos)

    def __eq__(self, other):
        return self.pos == other.pos

    def __lt__(self, other):
        return self.cost < other.cost  # Corrected logic for comparison

# A* search implementation
def aStar(self, current, end):
    openSet = set()
    openHeap = []
    closedSet = set()

    startNode = Node(None, current, 0 + self.manHatDist(current, end))
    openSet.add(startNode)
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openSet:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile in closedSet:
                continue

            newCost = curNode.cost + 1  # Assuming all moves have the same cost; modify if needed
            if tile not in openSet or newCost < tile.cost:
                tile.parent = curNode
                tile.cost = newCost + self.manHatDist(tile.pos, end)

                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []

# Example getAdjacentNodes method (assuming canMove and getLocIfMove are implemented)
def getAdjacentNodes(self, curPos):
    allMoves = ['North', 'South', 'East', 'West']
    posMoves = []
    for direction in allMoves:
        if self.canMove(direction, curPos):
            posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
    return posMoves
