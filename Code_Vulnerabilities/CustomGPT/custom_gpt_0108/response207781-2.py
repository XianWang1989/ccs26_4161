
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
        openHeap = []
        closedSet = set()
        startNode = Node(0, current, self.manHatDist(current, end))
        heapq.heappush(openHeap, (startNode.cost, startNode))

        while openHeap:
            _, curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tentative_cost = curNode.cost + 1  # Assumed cost of moving to adjacent tile

                if tentative_cost < tile.cost:
                    tile.parent = curNode
                    tile.cost = tentative_cost + self.manHatDist(tile.pos, end)

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
            if self.canMove(direction, curPos):
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))  # Cost will be set later
        return posMoves

    # Assume manHatDist, canMove, getLocIfMove methods are defined
