
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Corrected for proper heap behavior


def aStar(self, current, end):
    openSet = {}  # Using a dictionary for fast lookups
    openHeap = []  # Min-heap to store nodes
    closedSet = set()

    startNode = Node(0, current, self.manHatDist(current, end))
    openSet[startNode.pos] = startNode
    heapq.heappush(openHeap, startNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        del openSet[curNode.pos]  # Remove from openSet
        closedSet.add(curNode.pos)

        for tile in self.getAdjacentNodes(curNode.pos):
            if tile.pos in closedSet:
                continue

            # Calculate new cost with Manhattan distance
            g_score = curNode.cost + self.euclidDist(curNode.pos, tile.pos)
            if tile.pos not in openSet or g_score < tile.cost:
                tile.parent = curNode
                tile.cost = g_score + self.manHatDist(tile.pos, end)

                if tile.pos not in openSet:
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, tile)

    return []

def getDirections(self, endNode):
    moves = []
    while endNode.parent is not None:
        moves.append(endNode.value)
        endNode = endNode.parent
    moves.reverse()
    return moves  # Returns a list of moves from start to end
