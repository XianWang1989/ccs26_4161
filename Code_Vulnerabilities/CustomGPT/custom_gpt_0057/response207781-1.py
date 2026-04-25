
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
        openSet = set()
        openHeap = []

        startNode = Node("", current, self.manhattanDist(current, end))
        openSet.add(startNode)
        heapq.heappush(openHeap, (startNode.cost, startNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]
            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile not in openSet:
                    tile.parent = curNode
                    tile.cost = curNode.cost + 1 + self.manhattanDist(tile.pos, end)  # Using a new cost calculation
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))

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
            newPos = self.getLocIfMove(curPos, direction)
            if newPos:
                posMoves.append(Node(direction, newPos, 0))
        return posMoves

    def manhattanDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def getLocIfMove(self, curPos, direction):
        moves = {
            'North': (curPos[0], curPos[1] - 1),
            'South': (curPos[0], curPos[1] + 1),
            'East':  (curPos[0] + 1, curPos[1]),
            'West':  (curPos[0] - 1, curPos[1]),
        }
        return moves.get(direction, None)

    def canMove(self, direction, curPos):
        # Assuming a grid boundary check or obstacle check is implemented here
        return True  # Placeholder
