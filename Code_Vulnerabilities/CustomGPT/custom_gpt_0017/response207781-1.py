
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Ensure proper priority queue behavior

class AStar:
    def aStar(self, current, end):
        openHeap = []  # Min-heap for the open set
        openSet = {}   # Maps positions to nodes in the heap
        closedSet = set()  # Best path so far
        curNode = Node(0, current, self.manHatDist(current, end))

        openHeap.append(curNode)
        openSet[current] = curNode

        while openHeap:
            curNode = heapq.heappop(openHeap)
            openSet.pop(curNode.pos)  # Remove from openSet

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tentative_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos)

                if tile.pos not in openSet or tentative_cost < tile.cost:
                    tile.cost = tentative_cost + self.manHatDist(tile.pos, end)
                    tile.parent = curNode

                    if tile.pos not in openSet:
                        openSet[tile.pos] = tile
                        heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode:
            moves.append(endNode.value)
            endNode = endNode.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))
        return posMoves

    # Assume manHatDist and euclidDist methods are implemented here
