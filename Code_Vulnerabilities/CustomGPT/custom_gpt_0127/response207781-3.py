
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Corrected comparison

class AStar:
    def aStar(self, current, end):
        openSet = set()
        openHeap = []
        closedSet = set()

        startNode = Node(None, current, self.manHatDist(current, end))
        openSet.add(startNode)
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)
            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + curNode.cost

                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode.parent is not None:
            moves.append(endNode.value)
            endNode = endNode.parent
        return moves[::-1]  # Reverse the moves

    def getAdjacentNodes(self, curPos):
        # Implementation of adjacent nodes as in your example
        pass

    def manHatDist(self, pos1, pos2):
        # Implementation for Manhattan distance
        pass

