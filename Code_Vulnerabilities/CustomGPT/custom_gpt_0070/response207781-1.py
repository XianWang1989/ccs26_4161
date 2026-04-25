
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

class AStarAlgorithm:
    def aStar(self, current, end):
        openSet = {}  # Dictionary for faster lookups
        openHeap = []  # Priority queue for nodes
        closedSet = set()  # Explored nodes
        startNode = Node(None, current, 0)
        openSet[current] = startNode
        heapq.heappush(openHeap, (0, startNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]
            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.pop(curNode.pos)
            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                cost = curNode.cost + 1  # Assuming uniform cost for each step
                if tile.pos not in openSet or cost < openSet[tile.pos].cost:
                    tile.parent = curNode
                    tile.cost = cost + self.manHatDist(tile.pos, end)

                    if tile.pos not in openSet:
                        openSet[tile.pos] = tile
                        heapq.heappush(openHeap, (tile.cost, tile))

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

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    # Assuming other methods like canMove and getLocIfMove are implemented
