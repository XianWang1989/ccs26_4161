
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
    openHeap = []     # Priority queue for lowest cost
    closedSet = set() # Best path so far

    start_node = Node(None, current, self.manHatDist(current, end))
    openSet.add(start_node)
    heapq.heappush(openHeap, (start_node.cost, start_node))

    while openHeap:
        curNode = heapq.heappop(openHeap)[1]

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        closedSet.add(curNode)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile in closedSet:
                continue

            tentative_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos) + self.manHatDist(tile.pos, end)

            if tile not in openSet or tentative_cost < tile.cost:
                tile.parent = curNode
                tile.cost = tentative_cost

                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))

    return []

def getDirections(self, endNode):
    moves = []
    while endNode:
        if endNode.value:
            moves.append(endNode.value)
        endNode = endNode.parent
    return moves[::-1]
