
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
        openSet = set()  # Set of explorable nodes
        openHeap = []    # All paths heap, lowest cost on top
        closedSet = set()  # Best path so far
        curNode = Node(None, current, self.manHatDist(current, end))
        openSet.add(curNode)
        heapq.heappush(openHeap, curNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)
            openSet.remove(curNode)
            closedSet.add(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile not in closedSet:
                    tile.parent = curNode
                    tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current) + curNode.cost
                    if tile not in openSet:
                        openSet.add(tile)
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

    # Placeholder for Manhattan distance
    def manHatDist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    # Placeholder for Euclidean distance
    def euclidDist(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def getAdjacentNodes(self, curPos):
        allMoves = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in allMoves:
            if self.canMove(direction, curPos):
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves

    # Placeholder for movement permission
    def canMove(self, direction, curPos):
        # Implement movement logic based on grid world
        return True

    # Placeholder for getting new position based on direction
    def getLocIfMove(self, curPos, direction):
        if direction == 'North':
            return (curPos[0], curPos[1] + 1)
        elif direction == 'South':
            return (curPos[0], curPos[1] - 1)
        elif direction == 'East':
            return (curPos[0] + 1, curPos[1])
        elif direction == 'West':
            return (curPos[0] - 1, curPos[1])
