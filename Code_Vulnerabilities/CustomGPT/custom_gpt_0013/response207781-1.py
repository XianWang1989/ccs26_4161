
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    # Compare nodes based on their cost for the heap
    def __lt__(self, other):
        return self.cost < other.cost

class AStarPathfinder:
    def aStar(self, current, end):
        openSet = {}  # Dictionary to store open nodes
        openHeap = []  # Min-heap for the priority queue
        closedSet = set()  # Set to keep track of closed nodes

        startNode = Node(0, current, self.manHatDist(current, end))
        openSet[startNode.pos] = startNode
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

                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

                if tile.pos not in openSet or tile.cost < openSet[tile.pos].cost:
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode.parent is not None:
            moves.append(endNode.value)
            endNode = endNode.parent
        return moves[::-1]  # Reverse the list to get the correct order

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))
        return posMoves

    # Assume the definitions of manHatDist, euclidDist, canMove, and getLocIfMove exist
