
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
        openSet = {}  # Dictionary for O(1) lookups
        openHeap = []  # Min-heap for lowest cost
        closedSet = set()

        startNode = Node("", current, self.manHatDist(current, end))
        openSet[current] = startNode
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.pop(curNode.pos)
            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tentative_g_score = curNode.cost + 1  # Assuming uniform cost
                if tile.pos in openSet:
                    if tentative_g_score < openSet[tile.pos].cost:
                        openSet[tile.pos].cost = tentative_g_score
                        openSet[tile.pos].parent = curNode
                else:
                    tile.parent = curNode
                    tile.cost = tentative_g_score + self.manHatDist(tile.pos, end)
                    openSet[tile.pos] = tile
                    heapq.heappush(openHeap, tile)

        return []

    def getDirections(self, endNode):
        moves = []
        while endNode:
            moves.append(endNode.value)
            endNode = endNode.parent
        moves.pop()  # Remove the initial node's value (empty)
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

    def manHatDist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def euclidDist(self, a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

    def canMove(self, direction, curPos):
        # Implementation of movement validation
        pass

    def getLocIfMove(self, curPos, direction):
        # Implementation of getting new position if move is valid
        pass
