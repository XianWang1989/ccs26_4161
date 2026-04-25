
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.pos == other.pos


class AStar:
    def aStar(self, current, end):
        openSet = set()   # Set of explorable nodes
        openHeap = []     # All paths heap, lowest cost on top
        startNode = Node(None, current, 0)
        startNode.cost = self.manHatDist(current, end)

        openSet.add(startNode)
        heapq.heappush(openHeap, (startNode.cost, startNode))

        while openHeap:
            curNode = heapq.heappop(openHeap)[1]
            if curNode.pos == end:
                return self.getDirections(curNode)

            openSet.remove(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile not in openSet:
                    tile.parent = curNode
                    tile.cost = self.manHatDist(tile.pos, end) + curNode.cost + 1  # +1 for step cost

                    if tile not in openSet or tile.cost < curNode.cost:
                        openSet.add(tile)
                        heapq.heappush(openHeap, (tile.cost, tile))

        return []

    def getDirections(self, endNode):
        moves = []
        tmpNode = endNode
        while tmpNode and tmpNode.parent is not None:
            moves.append(tmpNode.value)
            tmpNode = tmpNode.parent
        moves.reverse()
        return moves

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def euclidDist(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def canMove(self, direction, pos):
        # Implement movement validation based on your grid conditions.
        pass

    def getLocIfMove(self, pos, direction):
        # Calculate new position based on direction.
        pass
