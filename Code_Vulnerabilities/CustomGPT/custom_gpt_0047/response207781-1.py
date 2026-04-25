
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class PathFinder:
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

                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

                # Check if tile is already in the heap
                if all(tile.pos != node[1].pos for node in openHeap):
                    heapq.heappush(openHeap, (tile.cost, tile))

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent:
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
