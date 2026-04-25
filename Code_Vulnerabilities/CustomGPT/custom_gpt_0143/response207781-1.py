
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class GridWorld:
    def aStar(self, current, end):
        openSet = {}  # Dictionary to track nodes in open set with costs
        openHeap = []  # Priority queue for nodes
        closedSet = set()  # Set of nodes already evaluated

        startNode = Node(None, current, 0 + self.manHatDist(current, end))
        openSet[current] = startNode
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tentative_cost = curNode.cost - self.manHatDist(curNode.pos, end) + self.euclidDist(curNode.pos, tile.pos) + self.manHatDist(tile.pos, end)

                if tile.pos not in openSet or tentative_cost < tile.cost:
                    tile.parent = curNode
                    tile.cost = tentative_cost
                    openSet[tile.pos] = tile
                    if tile not in openHeap:
                        heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                nextPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, nextPos, 0))
        return posMoves

    # Placeholder methods for distance calculations
    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def euclidDist(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5
