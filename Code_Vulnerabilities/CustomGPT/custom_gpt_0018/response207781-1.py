
import heapq

class Node:
    def __init__(self, value, pos, g_cost):
        self.pos = pos
        self.g_cost = g_cost     # Cost from start to current node
        self.h_cost = 0          # Heuristic cost (estimated cost to goal)
        self.value = value
        self.parent = None

    @property
    def cost(self):
        return self.g_cost + self.h_cost

    def __lt__(self, other):
        return self.cost < other.cost  # Corrected comparison

def aStar(self, current, end):
    openSet = set()          # Set of explorable nodes
    openHeap = []           # All paths heap, lowest cost on top
    curNode = Node(None, current, 0)
    curNode.h_cost = self.manHatDist(current, end)
    openSet.add(curNode)
    heapq.heappush(openHeap, curNode)

    while openHeap:
        curNode = heapq.heappop(openHeap)

        if curNode.pos == end:
            return self.getDirections(curNode)

        openSet.remove(curNode)
        for tile in self.getAdjacentNodes(curNode.pos):
            if tile not in openSet:
                tile.parent = curNode
                tile.g_cost = curNode.g_cost + 1  # assuming each move has a cost of 1
                tile.h_cost = self.manHatDist(tile.pos, end)

                # Push tile into the open set
                openSet.add(tile)
                heapq.heappush(openHeap, tile)

    return []

def getDirections(self, endNode):
    moves = []
    while endNode:
        if endNode.value:
            moves.append(endNode.value)
        endNode = endNode.parent
    moves.reverse()
    return moves
