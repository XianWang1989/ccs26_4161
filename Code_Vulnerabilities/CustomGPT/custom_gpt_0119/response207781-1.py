
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
        openSet = {}  # Using dict to store nodes with their costs
        openHeap = []  # Heap for path exploration
        closedSet = set()

        # Initialize starting node
        startNode = Node(None, current, self.manHatDist(current, end))
        openSet[current] = startNode
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)
            del openSet[curNode.pos]

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                newCost = curNode.cost + self.euclidDist(curNode.pos, tile.pos) + self.manHatDist(tile.pos, end)
                if tile.pos not in openSet or newCost < openSet[tile.pos].cost:
                    tile.cost = newCost
                    tile.parent = curNode
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode is not None:
            if endNode.value is not None:
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
                posMoves.append(Node(direction, newPos, 0))  # Cost set to 0 initially
        return posMoves
