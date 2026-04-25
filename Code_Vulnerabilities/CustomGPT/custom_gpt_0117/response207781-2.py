
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
        openSet = set()   # Set of explorable nodes
        openHeap = []     # Min-heap for the nodes to be explored
        closedSet = {}    # Dictionary for best path so far

        startNode = Node('Start', current, self.manHatDist(current, end))
        openSet.add(startNode)
        heapq.heappush(openHeap, (startNode.cost, startNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]

            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)
            closedSet[curNode.pos] = curNode

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tile.parent = curNode
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current)

                if tile not in openSet:
                    openSet.add(tile)
                    heapq.heappush(openHeap, (tile.cost, tile))

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
                nextPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, nextPos, 0))
        return posMoves

    # Placeholder for heuristic functions
    def manHatDist(self, current, end):
        return abs(current[0] - end[0]) + abs(current[1] - end[1])

    def euclidDist(self, current, end):
        return ((current[0] - end[0]) ** 2 + (current[1] - end[1]) ** 2) ** 0.5

    def canMove(self, direction, curPos):
        # Implement movement logic
        pass

    def getLocIfMove(self, curPos, direction):
        # Implement movement logic to find new position
        pass
