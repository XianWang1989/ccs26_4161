
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
    openSet = set()  # Set of explorable nodes
    openHeap = []    # Min-heap priority queue
    closedSet = set()  # Explored nodes

    startNode = Node(0, current, self.manHatDist(current, end))
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

            newCost = curNode.cost + self.euclidDist(curNode.pos, tile.pos) + self.manHatDist(tile.pos, end)

            if tile not in openSet or newCost < tile.cost:
                tile.cost = newCost
                tile.parent = curNode

                if tile not in openSet:
                    openSet.add(tile)
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
