
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
        openSet = {}
        openHeap = []
        closedSet = set()

        startNode = Node('', current, 0)
        startNode.cost = self.manHatDist(current, end)
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

                tile.parent = curNode
                tile.cost = curNode.cost + 1 + self.manHatDist(tile.pos, end)  # Adding 1 for the move cost

                if tile.pos not in openSet or tile.cost < openSet[tile.pos].cost:
                    openSet[tile.pos] = tile
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
        directions = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in directions:
            if self.canMove(direction, curPos):
                newPos = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newPos, 0))
        return posMoves

    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def euclidDist(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    # Placeholder methods
    def canMove(self, direction, curPos):
        # Implement movement logic
        return True

    def getLocIfMove(self, curPos, direction):
        # Implement logic to return new position
        return curPos
