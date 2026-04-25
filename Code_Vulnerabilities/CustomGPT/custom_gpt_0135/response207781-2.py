
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):  # Correct implementation for priority queue
        return self.cost < other.cost

class PathFinder:
    def aStar(self, current, end):
        openHeap = []  # Min-heap for the nodes
        startNode = Node("", current, self.manHatDist(current, end))
        heapq.heappush(openHeap, startNode)

        closedSet = {}
        while openHeap:
            curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            if curNode.pos in closedSet and closedSet[curNode.pos] <= curNode.cost:
                continue

            closedSet[curNode.pos] = curNode.cost

            for tile in self.getAdjacentNodes(curNode.pos):
                tile.cost = self.manHatDist(tile.pos, end) + curNode.cost
                # Only add to open set if it's not in the closedSet or has a lower cost
                if tile.pos not in closedSet or closedSet[tile.pos] > tile.cost:
                    tile.parent = curNode
                    heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        return moves[::-1]  # Return reversed list

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))  # Cost will be set in aStar
        return posMoves

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
