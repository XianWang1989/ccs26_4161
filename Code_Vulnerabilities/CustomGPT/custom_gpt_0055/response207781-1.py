
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Correct comparison

    def __hash__(self):
        return hash(self.pos)  # Allows using in sets

    def __eq__(self, other):
        return self.pos == other.pos  # Allows comparison based on position

class AStar:
    def aStar(self, current, end):
        openSet = {}  # Node's position as key, node as value
        openHeap = []  # Min-heap based on costs
        closedSet = set()

        startNode = Node(None, current, 0)
        openSet[current] = startNode
        heapq.heappush(openHeap, (startNode.cost, startNode))

        while openHeap:
            _, curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode)
            for tile in self.getAdjacentNodes(curNode.pos):
                if tile in closedSet:
                    continue

                cost = curNode.cost + 1  # Adjust based on movement cost
                if tile not in openSet or cost < openSet[tile].cost:
                    tile.cost = cost + self.manHatDist(tile.pos, end)
                    tile.parent = curNode
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, (tile.cost, tile))

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        return moves[::-1]

    def getAdjacentNodes(self, curPos):
        # Return all possible moves from given tile as Node objects
        # Assume directions and canMove & getLocIfMove methods already defined
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))
        return posMoves

    # Assume manHatDist() is defined
