
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class Pathfinding:
    # A* search algorithm
    def aStar(self, current, end):
        openSet = set()   # Set of explorable nodes
        openHeap = []     # All paths heap, lowest cost on top
        startNode = Node("", current, 0)
        startNode.cost = self.manHatDist(current, end)

        openSet.add(startNode)
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in openSet:
                    continue

                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + curNode.cost

                if tile.pos not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
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

    def manHatDist(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    # Add Euclidean distance method here if needed...
