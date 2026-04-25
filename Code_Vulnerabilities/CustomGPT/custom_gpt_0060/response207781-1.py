
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Correct comparison

class AStarPathfinder:
    def aStar(self, current, end):
        openSet = set()   # Set of explorable nodes
        openHeap = []     # All paths heap, lowest cost on top
        closedSet = {}    # Best path so far with node as keys
        curNode = Node(None, current, self.manHatDist(current, end))
        openSet.add(curNode)
        heapq.heappush(openHeap, curNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)
            openSet.remove(curNode)
            closedSet[curNode.pos] = curNode

            for direction, adjacentPos in self.getAdjacentNodes(curNode.pos):
                if adjacentPos in closedSet:
                    continue

                tile = Node(direction, adjacentPos, self.manHatDist(adjacentPos, end) + curNode.cost + 1)  # +1 for movement cost
                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, tile)

        return []

    # Returns both the direction and the position of the adjacent node
    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                newPos = self.getLocIfMove(curPos, direction)  # Assuming this method returns the new position
                posMoves.append((direction, newPos))
        return posMoves

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        moves.reverse()
        return moves

    # Assume manHatDist and euclidDist are defined elsewhere
    # and canMove, getLocIfMove methods are already implemented.
