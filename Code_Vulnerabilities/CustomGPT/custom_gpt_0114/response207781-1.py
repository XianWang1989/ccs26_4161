
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class Pathfinder:
    def aStar(self, current, end):
        openSet = set()
        openHeap = []
        closedSet = set()
        startNode = Node(0, current, self.manHatDist(current, end))
        openSet.add(startNode)
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)
            closedSet.add(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile not in closedSet:
                    tentative_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos)
                    if tile not in openSet or tentative_cost < tile.cost:
                        tile.parent = curNode
                        tile.cost = tentative_cost + self.manHatDist(tile.pos, end)
                        if tile not in openSet:
                            openSet.add(tile)
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
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))
        return posMoves
