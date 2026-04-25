
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.pos == other.pos

def aStar(self, current, end):
    openSet = set()   # Set of explorable nodes
    openHeap = []     # Priority queue for nodes sorted by cost
    closedSet = set() # Best path so far
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
            if tile not in closedSet:
                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current) + curNode.cost

                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))
                else:
                    # Update the cost if lower
                    for index, (cost, node) in enumerate(openHeap):
                        if node == tile and tile.cost < cost:
                            openHeap[index] = (tile.cost, tile)
                            heapq.heapify(openHeap)
                            break

    return []

def getDirections(self, endNode):
    moves = []
    while endNode.parent is not None:
        moves.append(endNode.value)
        endNode = endNode.parent
    return moves[::-1]
