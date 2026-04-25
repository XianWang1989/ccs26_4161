
import heapq

class Node:
    def __init__(self, value, pos, cost):
        self.pos = pos
        self.cost = cost
        self.value = value
        self.parent = None

    def __lt__(self, other):
        return self.cost < other.cost  # Correct comparison for heap

class AStarSearch:
    def aStar(self, current, end):
        openSet = []  # Use a priority queue for open set
        closedSet = set()  # Keep track of visited nodes

        startNode = Node(0, current, self.manHatDist(current, end))
        heapq.heappush(openSet, startNode)

        while openSet:
            curNode = heapq.heappop(openSet)

            if curNode.pos == end:
                return self.getDirections(curNode)

            closedSet.add(curNode.pos)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile.pos in closedSet:
                    continue

                tile.parent = curNode
                # Update the cost using a single heuristic function
                tile.cost = self.manHatDist(tile.pos, end) + self.euclidDist(tile.pos, current) + curNode.cost

                # Only add non-visited nodes to the open set
                if tile not in openSet:
                    heapq.heappush(openSet, tile)

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
                posMoves.append(Node(direction, self.getLocIfMove(curPos, direction), 0))
        return posMoves

    # Placeholder for actual distance functions
    def manHatDist(self, current, end):
        return abs(current[0] - end[0]) + abs(current[1] - end[1])

    def euclidDist(self, current, end):
        return ((current[0] - end[0]) ** 2 + (current[1] - end[1]) ** 2) ** 0.5
