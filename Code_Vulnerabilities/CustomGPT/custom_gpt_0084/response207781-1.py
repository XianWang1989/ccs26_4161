
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost


class AStarPathFinder:
    def aStar(self, current, end):
        openHeap = []  # priority queue for exploring nodes
        closedSet = set()  # set of explored nodes
        startNode = Node(None, current, self.manHatDist(current, end))

        heapq.heappush(openHeap, (startNode.cost, startNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tile.parent = curNode
                tile.cost = self.calculateCost(tile.pos, end, curNode.cost)

                # Add to open set only if it's not already there
                if not any(tile.pos == n[1].pos and tile.cost >= n[1].cost for n in openHeap):
                    heapq.heappush(openHeap, (tile.cost, tile))

        return []

    def calculateCost(self, tilePos, end, currentCost):
        return currentCost + self.manHatDist(tilePos, end)

    def getDirections(self, endNode):
        moves = []
        while endNode is not None:
            if endNode.value:
                moves.append(endNode.value)
            endNode = endNode.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves
