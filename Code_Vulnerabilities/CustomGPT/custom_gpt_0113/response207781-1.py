
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class AStarSearch:
    def aStar(self, current, end):
        openSet = {}  # Dictionary to store nodes
        openHeap = []  # Priority queue for nodes
        closedSet = set()  # Explored nodes

        startNode = Node(0, current, self.manHatDist(current, end))
        openSet[current] = startNode
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)
            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                g_cost = curNode.cost + 1  # Use a simple cost to move to adjacent tile
                if tile.pos not in openSet or g_cost < tile.cost:
                    tile.parent = curNode
                    tile.cost = g_cost + self.manHatDist(tile.pos, end)
                    openSet[tile.pos] = tile
                    if tile not in openHeap:
                        heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode.parent is not None:
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
                posMoves.append(Node(direction, newPos, 0))
        return posMoves

    # Implement other methods like canMove, getLocIfMove, manHatDist, etc.
