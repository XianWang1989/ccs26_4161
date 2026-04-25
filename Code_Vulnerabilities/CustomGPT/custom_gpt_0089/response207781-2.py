
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

    def __hash__(self):
        return hash(self.pos)

class AStarSearch:
    def aStar(self, current, end):
        openSet = {}  # Use a dictionary for faster lookups
        openHeap = []  # Min-heap for the best paths
        closedSet = set()

        startNode = Node("", current, 0)
        startNode.cost = self.manHatDist(current, end)
        openSet[startNode] = startNode.cost
        heapq.heappush(openHeap, startNode)

        while openHeap:
            curNode = heapq.heappop(openHeap)
            if curNode.pos == end:
                return self.getDirections(curNode)
            closedSet.add(curNode)

            for tile in self.getAdjacentNodes(curNode.pos):
                if tile in closedSet:
                    continue

                tentative_cost = curNode.cost + 1  # Assume uniform cost for simplicity
                if tile not in openSet or tentative_cost < tile.cost:
                    tile.parent = curNode
                    tile.cost = tentative_cost + self.manHatDist(tile.pos, end)
                    if tile not in openSet:
                        openSet[tile] = tile.cost
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
        # Assume canMove and getLocIfMove are defined elsewhere
        directions = ['North', 'South', 'East', 'West']
        posMoves = []
        for direction in directions:
            if self.canMove(direction, curPos):
                newLoc = self.getLocIfMove(curPos, direction)
                posMoves.append(Node(direction, newLoc, 0))
        return posMoves
