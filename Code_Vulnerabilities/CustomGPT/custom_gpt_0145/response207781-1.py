
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class AStarAlgorithm:
    def aStar(self, current, end):
        openSet = [] # This serves as the priority queue
        closedSet = {} # Using dictionary for fast look-up

        startNode = Node(0, current, self.manHatDist(current, end))
        heapq.heappush(openSet, (startNode.cost, startNode))

        while openSet:
            curNode = heapq.heappop(openSet)[1]
            if curNode.pos == end:
                return self.getDirections(curNode)

            # Add current node to closedSet
            closedSet[curNode.pos] = curNode

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet: 
                    continue  # Already evaluated

                tile.parent = curNode
                tile.cost = self.manHatDist(curNode.pos, end) + self.euclidDist(curNode.pos, current) + curNode.cost

                # If in openSet, check for a better path.
                if (tile.cost, tile) not in openSet: 
                    heapq.heappush(openSet, (tile.cost, tile))

        return []  # No path found

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
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves

    def manHatDist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def euclidDist(self, a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
