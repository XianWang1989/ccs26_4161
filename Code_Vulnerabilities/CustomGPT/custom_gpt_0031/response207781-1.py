
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash(self.pos)

    def __eq__(self, other):
        return self.pos == other.pos

class GridWorld:
    def aStar(self, current, end):
        openSet = set()
        openHeap = []
        closedSet = set()

        startNode = Node("", current, 0)
        startNode.heuristic = self.manHatDist(current, end)
        openSet.add(startNode)
        heapq.heappush(openHeap, (startNode.heuristic, startNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]

            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)
            closedSet.add(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile in closedSet:
                    continue

                tile.parent = curNode
                tile.cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos) + self.manHatDist(tile.pos, end)

                if tile not in openSet or tile.cost < curNode.cost:
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost + tile.heuristic, tile))

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
                posMoves.append(Node(direction, newPos, 0))  # Cost is calculated during pathfinding
        return posMoves

    # Assuming these methods are defined
    def manHatDist(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def euclidDist(self, point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

    def canMove(self, direction, pos):
        # Implement movement logic
        pass

    def getLocIfMove(self, curPos, direction):
        # Implement logic to get new position based on direction
        pass
