
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
        openSet = []
        closedSet = {}
        startNode = Node('', current, 0)
        heapq.heappush(openSet, startNode)

        while openSet:
            curNode = heapq.heappop(openSet)
            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet[curNode.pos] = curNode

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tentative_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos)
                if all(tentative_cost < node.cost for node in openSet if node.pos == tile.pos):
                    tile.cost = tentative_cost + self.manHatDist(tile.pos, end)
                    tile.parent = curNode
                    heapq.heappush(openSet, tile)

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
        directions = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in directions:
            if self.canMove(direction, curPos):
                nextPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, nextPos, 0))
        return posMoves

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def euclidDist(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5
