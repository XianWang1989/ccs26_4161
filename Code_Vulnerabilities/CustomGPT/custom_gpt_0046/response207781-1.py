
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Correctly define less than for heap

class AStar:
    def aStar(self, current, end):
        openSet = {}  # Use a dictionary to store nodes in openSet
        openHeap = []  # Priority queue for exploration
        closedSet = set()

        startNode = Node(None, current, 0)
        startNode.heuristic = self.manHatDist(current, end)
        startNode.cost = startNode.heuristic
        openSet[current] = startNode

        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)

            if curNode.pos == end:
                return self.getDirections(curNode)

            del openSet[curNode.pos]
            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tentative_cost = curNode.cost + self.euclidDist(curNode.pos, tile.pos)

                if tile.pos not in openSet or tentative_cost < openSet[tile.pos].cost:
                    tile.parent = curNode
                    tile.cost = tentative_cost + self.manHatDist(tile.pos, end)
                    openSet[tile.pos] = tile
                    if tile not in openHeap:
                        heapq.heappush(openHeap, tile)

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
        allMoves = ['North','South','East','West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves

    def manHatDist(self, pos1, pos2):
        # Implement Manhattan distance calculation
        pass

    def euclidDist(self, pos1, pos2):
        # Implement Euclidean distance calculation
        pass
