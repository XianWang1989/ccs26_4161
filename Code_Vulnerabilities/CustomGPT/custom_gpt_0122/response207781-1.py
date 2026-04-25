
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
    openHeap = []     # Priority queue for paths
    closedSet = set() # Explored nodes
    startNode = Node(None, current, 0)
    startNode.cost = self.manHatDist(current, end)
    openSet.add(startNode)
    heapq.heappush(openHeap, (startNode.cost, startNode))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile in closedSet:
                continue

            tile_cost = self.euclidDist(current, tile.pos) + self.manHatDist(tile.pos, end)
            if tile not in openSet or tile.cost > tile_cost:
                tile.parent = curNode
                tile.cost = tile_cost

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
