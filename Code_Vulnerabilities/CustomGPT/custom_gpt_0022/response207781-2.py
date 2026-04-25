
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class AStar:
    def aStar(self, current, end):
        openHeap = []  # Priority queue for exploring nodes
        closedSet = set()  # Best path so far
        startNode = Node(0, current, self.manHatDist(current, end))
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)
            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                new_cost = self.manHatDist(tile.pos, end) + curNode.cost + self.euclidDist(tile.pos, current)
                if tile not in [n for _, n in openHeap] or new_cost < tile.cost:
                    tile.cost = new_cost
                    tile.parent = curNode
                    heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode.parent is not None:
            moves.append(endNode.value)
            endNode = endNode.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves

    def manHatDist(self, a, b):
        # Implement the Manhattan distance calculation
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def euclidDist(self, a, b):
        # Implement the Euclidean distance calculation
        return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5

    def canMove(self, direction, curPos):
        # Implement logic to check if a move is possible
        pass

    def getLocIfMove(self, curPos, direction):
        # Implement logic to get the new position if moving in a direction
        pass
